from __future__ import annotations

import uuid
from pathlib import Path
from typing import Final

from fastapi import UploadFile


ALLOWED_CONTENT_TYPES: Final[set[str]] = {
    "application/pdf",
    "text/plain",
    "text/markdown",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
}

ALLOWED_EXTENSIONS: Final[set[str]] = {
    ".pdf",
    ".txt",
    ".md",
    ".docx",
}

MAX_FILE_SIZE_BYTES: Final[int] = 20 * 1024 * 1024  # 20 MB


class FileValidationError(ValueError):
    pass


class LocalStorageService:
    def __init__(self, upload_dir: str = "data/uploads") -> None:
        self.upload_dir = Path(upload_dir)
        self.upload_dir.mkdir(parents=True, exist_ok=True)

    def validate_file(self, file: UploadFile, file_size: int) -> None:
        filename = file.filename or ""
        extension = Path(filename).suffix.lower()

        if not filename:
            raise FileValidationError("No file name provided.")

        if extension not in ALLOWED_EXTENSIONS:
            raise FileValidationError(
                f"Unsupported file extension: {extension}. "
                f"Allowed extensions: {', '.join(sorted(ALLOWED_EXTENSIONS))}"
            )

        if file.content_type not in ALLOWED_CONTENT_TYPES:
            raise FileValidationError(
                f"Unsupported content type: {file.content_type}. "
                f"Allowed content types: {', '.join(sorted(ALLOWED_CONTENT_TYPES))}"
            )

        if file_size <= 0:
            raise FileValidationError("Uploaded file is empty.")

        if file_size > MAX_FILE_SIZE_BYTES:
            raise FileValidationError(
                f"File exceeds maximum allowed size of {MAX_FILE_SIZE_BYTES // (1024 * 1024)} MB."
            )

    async def save_upload(self, file: UploadFile) -> dict:
        contents = await file.read()
        file_size = len(contents)

        self.validate_file(file, file_size)

        original_filename = Path(file.filename or "document").name
        extension = Path(original_filename).suffix.lower()
        document_id = str(uuid.uuid4())
        stored_filename = f"{document_id}{extension}"
        stored_path = self.upload_dir / stored_filename

        stored_path.write_bytes(contents)

        return {
            "document_id": document_id,
            "filename": original_filename,
            "content_type": file.content_type or "application/octet-stream",
            "size_bytes": file_size,
            "stored_path": str(stored_path).replace("\\", "/"),
            "status": "uploaded",
        }