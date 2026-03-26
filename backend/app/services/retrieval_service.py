import json
from pathlib import Path
from typing import Any

import numpy as np
from sentence_transformers import SentenceTransformer

from backend.app.schemas.retrieval import RetrievedChunk, RetrievalResponse


class RetrievalService:
    def __init__(self) -> None:
        self.model_name = "sentence-transformers/all-MiniLM-L6-v2"
        self.vector_store_dir = Path("vector_store") / "local_index"
        self.manifest_path = self.vector_store_dir / "manifest.json"
        self.processed_chunks_dir = Path("data") / "processed" / "chunks"
        self._model: SentenceTransformer | None = None

    @property
    def model(self) -> SentenceTransformer:
        if self._model is None:
            self._model = SentenceTransformer(self.model_name)
        return self._model

    def retrieve(self, query: str, top_k: int = 5) -> RetrievalResponse:
        query = query.strip()
        if not query:
            raise ValueError("Query cannot be empty.")

        manifest = self._load_manifest()
        documents = manifest.get("documents", {})

        if not documents:
            raise ValueError("Vector store is empty. No stored documents available.")

        query_vector = self.model.encode(
            query,
            convert_to_numpy=True,
            normalize_embeddings=True,
            show_progress_bar=False,
        )

        all_results: list[RetrievedChunk] = []

        for document_id, doc_info in documents.items():
            embedding_file_path = Path(doc_info["embedding_file_path"])
            stored_document_path = Path(doc_info["stored_document_path"])
            chunk_file_path = self.processed_chunks_dir / f"{document_id}.json"

            if not embedding_file_path.exists():
                continue
            if not stored_document_path.exists():
                continue
            if not chunk_file_path.exists():
                continue

            embeddings = np.load(embedding_file_path)
            stored_document = json.loads(stored_document_path.read_text(encoding="utf-8"))
            chunk_payload = json.loads(chunk_file_path.read_text(encoding="utf-8"))

            chunks_by_index = {
                int(chunk["chunk_index"]): chunk
                for chunk in chunk_payload
            }

            chunk_registry = stored_document.get("chunks", [])

            if len(chunk_registry) != len(embeddings):
                continue

            scores = embeddings @ query_vector

            for i, score in enumerate(scores):
                chunk_meta = chunk_registry[i]
                chunk_index = int(chunk_meta["chunk_index"])
                full_chunk = chunks_by_index.get(chunk_index)

                if not full_chunk:
                    continue

                all_results.append(
                    RetrievedChunk(
                        document_id=document_id,
                        chunk_id=full_chunk["chunk_id"],
                        chunk_index=chunk_index,
                        source_filename=full_chunk["source_filename"],
                        score=float(score),
                        char_start=int(full_chunk["char_start"]),
                        char_end=int(full_chunk["char_end"]),
                        token_estimate=full_chunk.get("token_estimate"),
                        text=full_chunk["text"],
                    )
                )

        ranked_results = sorted(
            all_results,
            key=lambda item: item.score,
            reverse=True,
        )[:top_k]

        return RetrievalResponse(
            query=query,
            top_k=top_k,
            result_count=len(ranked_results),
            results=ranked_results,
        )

    def _load_manifest(self) -> dict[str, Any]:
        if not self.manifest_path.exists():
            raise FileNotFoundError(
                f"Vector store manifest not found: {self.manifest_path}"
            )

        return json.loads(self.manifest_path.read_text(encoding="utf-8"))