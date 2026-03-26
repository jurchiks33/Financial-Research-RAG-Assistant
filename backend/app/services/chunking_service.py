import json
import uuid
from pathlib import Path
from typing import Any

from backend.app.schemas.chunk import ChunkResponse


class ChunkingService:
    def __init__(self) -> None:
        self.base_data_dir = Path("data")
        self.cleaned_dir = self.base_data_dir / "processed" / "cleaned_text"
        self.parsed_dir = self.base_data_dir / "processed" / "parsed_documents"
        self.chunks_dir = self.base_data_dir / "processed" / "chunks"

    def chunk_document(
        self,
        document_id: str,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ) -> ChunkResponse:
        if chunk_overlap >= chunk_size:
            raise ValueError("chunk_overlap must be smaller than chunk_size.")

        cleaned_file_path = self.cleaned_dir / f"{document_id}.txt"
        parsed_file_path = self.parsed_dir / f"{document_id}.json"

        if not cleaned_file_path.exists():
            raise FileNotFoundError(
                f"Cleaned text file not found for document_id={document_id}"
            )

        if not parsed_file_path.exists():
            raise FileNotFoundError(
                f"Parsed document file not found for document_id={document_id}"
            )

        text = cleaned_file_path.read_text(encoding="utf-8").strip()
        parsed_payload = json.loads(parsed_file_path.read_text(encoding="utf-8"))

        source_filename = parsed_payload.get("filename", f"{document_id}.txt")

        if not text:
            raise ValueError("Cleaned text is empty. Cannot create chunks.")

        chunks = self._build_chunks(
            text=text,
            document_id=document_id,
            source_filename=source_filename,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

        self.chunks_dir.mkdir(parents=True, exist_ok=True)
        output_path = self.chunks_dir / f"{document_id}.json"
        output_path.write_text(
            json.dumps(chunks, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

        return ChunkResponse(
            document_id=document_id,
            source_filename=source_filename,
            status="success",
            message="Document chunked successfully.",
            chunk_count=len(chunks),
            output_path=str(output_path),
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

    def _build_chunks(
        self,
        text: str,
        document_id: str,
        source_filename: str,
        chunk_size: int,
        chunk_overlap: int,
    ) -> list[dict[str, Any]]:
        chunks: list[dict[str, Any]] = []
        start = 0
        chunk_index = 0
        step = chunk_size - chunk_overlap

        while start < len(text):
            end = min(start + chunk_size, len(text))
            chunk_text = text[start:end].strip()

            if chunk_text:
                chunk_id = str(uuid.uuid4())
                token_estimate = max(1, len(chunk_text) // 4)

                chunks.append(
                    {
                        "chunk_id": chunk_id,
                        "document_id": document_id,
                        "source_filename": source_filename,
                        "chunk_index": chunk_index,
                        "char_start": start,
                        "char_end": end,
                        "chunk_size": len(chunk_text),
                        "overlap": chunk_overlap,
                        "token_estimate": token_estimate,
                        "text": chunk_text,
                    }
                )
                chunk_index += 1

            if end >= len(text):
                break

            start += step

        return chunks