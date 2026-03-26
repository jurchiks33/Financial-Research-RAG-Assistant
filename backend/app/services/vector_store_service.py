import json
from pathlib import Path
from typing import Any

from backend.app.schemas.vector_store import VectorStoreResponse


class VectorStoreService:
    def __init__(self) -> None:
        self.index_name = "local_financial_rag_index"
        self.base_data_dir = Path("data")
        self.embeddings_dir = self.base_data_dir / "embeddings" / "local_cache"
        self.vector_store_dir = Path("vector_store") / "local_index"
        self.manifest_path = self.vector_store_dir / "manifest.json"

    def store_document_vectors(self, document_id: str) -> VectorStoreResponse:
        embedding_file_path = self.embeddings_dir / f"{document_id}.npy"
        embedding_metadata_path = self.embeddings_dir / f"{document_id}.json"

        if not embedding_file_path.exists():
            raise FileNotFoundError(
                f"Embedding file not found for document_id={document_id}"
            )

        if not embedding_metadata_path.exists():
            raise FileNotFoundError(
                f"Embedding metadata file not found for document_id={document_id}"
            )

        if self.vector_store_dir.exists() and not self.vector_store_dir.is_dir():
            raise ValueError(
                f"Vector store path exists but is not a directory: {self.vector_store_dir}"
            )

        self.vector_store_dir.mkdir(parents=True, exist_ok=True)

        embedding_metadata = json.loads(
            embedding_metadata_path.read_text(encoding="utf-8")
        )

        stored_document_path = self.vector_store_dir / f"{document_id}.json"

        stored_document_payload: dict[str, Any] = {
            "document_id": document_id,
            "index_name": self.index_name,
            "model_name": embedding_metadata["model_name"],
            "embedding_count": embedding_metadata["embedding_count"],
            "embedding_dimension": embedding_metadata["embedding_dimension"],
            "embedding_file_path": str(embedding_file_path),
            "embedding_metadata_path": str(embedding_metadata_path),
            "chunks": embedding_metadata["chunks"],
        }

        stored_document_path.write_text(
            json.dumps(stored_document_payload, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

        manifest = self._load_manifest()
        manifest["index_name"] = self.index_name
        manifest["documents"][document_id] = {
            "document_id": document_id,
            "model_name": embedding_metadata["model_name"],
            "embedding_count": embedding_metadata["embedding_count"],
            "embedding_dimension": embedding_metadata["embedding_dimension"],
            "stored_document_path": str(stored_document_path),
            "embedding_file_path": str(embedding_file_path),
            "embedding_metadata_path": str(embedding_metadata_path),
        }

        self.manifest_path.write_text(
            json.dumps(manifest, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

        return VectorStoreResponse(
            document_id=document_id,
            status="success",
            message="Vectors stored successfully.",
            index_name=self.index_name,
            vector_count=int(embedding_metadata["embedding_count"]),
            embedding_dimension=int(embedding_metadata["embedding_dimension"]),
            manifest_path=str(self.manifest_path),
            stored_document_path=str(stored_document_path),
        )

    def _load_manifest(self) -> dict[str, Any]:
        if not self.manifest_path.exists():
            return {
                "index_name": self.index_name,
                "documents": {},
            }

        return json.loads(self.manifest_path.read_text(encoding="utf-8"))