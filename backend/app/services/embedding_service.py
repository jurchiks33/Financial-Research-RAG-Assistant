import json
from pathlib import Path
from typing import Any

import numpy as np
from sentence_transformers import SentenceTransformer

from backend.app.schemas.embedding import EmbeddingResponse


class EmbeddingService:
    def __init__(self) -> None:
        self.base_data_dir = Path("data")
        self.chunks_dir = self.base_data_dir / "processed" / "chunks"
        self.embeddings_dir = self.base_data_dir / "embeddings" / "local_cache"
        self.model_name = "sentence-transformers/all-MiniLM-L6-v2"
        self._model: SentenceTransformer | None = None

    @property
    def model(self) -> SentenceTransformer:
        if self._model is None:
            self._model = SentenceTransformer(self.model_name)
        return self._model

    def embed_document(self, document_id: str) -> EmbeddingResponse:
        chunk_file_path = self.chunks_dir / f"{document_id}.json"

        if not chunk_file_path.exists():
            raise FileNotFoundError(
                f"Chunk file not found for document_id={document_id}"
            )

        chunks = json.loads(chunk_file_path.read_text(encoding="utf-8"))

        if not chunks:
            raise ValueError("Chunk file is empty. Cannot generate embeddings.")

        texts = [chunk["text"] for chunk in chunks if chunk.get("text")]

        if not texts:
            raise ValueError("No chunk text found. Cannot generate embeddings.")

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=True,
            show_progress_bar=False,
        )

        self.embeddings_dir.mkdir(parents=True, exist_ok=True)

        embeddings_output_path = self.embeddings_dir / f"{document_id}.npy"
        metadata_output_path = self.embeddings_dir / f"{document_id}.json"

        np.save(embeddings_output_path, embeddings)

        metadata_payload: dict[str, Any] = {
            "document_id": document_id,
            "model_name": self.model_name,
            "embedding_count": int(embeddings.shape[0]),
            "embedding_dimension": int(embeddings.shape[1]),
            "chunks": [
                {
                    "chunk_id": chunk["chunk_id"],
                    "chunk_index": chunk["chunk_index"],
                    "source_filename": chunk["source_filename"],
                    "char_start": chunk["char_start"],
                    "char_end": chunk["char_end"],
                    "token_estimate": chunk.get("token_estimate"),
                }
                for chunk in chunks
            ],
        }

        metadata_output_path.write_text(
            json.dumps(metadata_payload, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

        return EmbeddingResponse(
            document_id=document_id,
            status="success",
            message="Embeddings generated successfully.",
            model_name=self.model_name,
            embedding_count=int(embeddings.shape[0]),
            embedding_dimension=int(embeddings.shape[1]),
            embeddings_output_path=str(embeddings_output_path),
            metadata_output_path=str(metadata_output_path),
        )