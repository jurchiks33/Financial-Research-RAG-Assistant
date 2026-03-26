import uuid
from pathlib import Path

from backend.app.schemas.document import DocumentProcessResponse
from backend.app.services.parser_service import ParserService
from backend.app.utils.file_loader import save_json_file, save_text_file
from backend.app.utils.metadata_extractor import build_document_metadata
from backend.app.utils.text_cleaner import preprocess_text


class IngestionService:
    def __init__(self) -> None:
        self.parser_service = ParserService()

        self.base_data_dir = Path("data")
        self.uploads_dir = self.base_data_dir / "uploads"
        self.processed_dir = self.base_data_dir / "processed"
        self.parsed_dir = self.processed_dir / "parsed_documents"
        self.cleaned_dir = self.processed_dir / "cleaned_text"
        self.metadata_dir = self.processed_dir / "metadata"

    def process_uploaded_document(self, filename: str) -> DocumentProcessResponse:
        file_path = self.uploads_dir / filename

        if not file_path.exists():
            raise FileNotFoundError(f"Uploaded file not found: {file_path}")

        document_id = str(uuid.uuid4())

        parsed = self.parser_service.parse(file_path)
        cleaned_text = preprocess_text(parsed.raw_text)

        metadata = build_document_metadata(
            document_id=document_id,
            file_path=file_path,
            file_type=parsed.file_type,
            file_size=file_path.stat().st_size,
            page_count=parsed.page_count,
            title=parsed.title,
        )

        parsed_output_path = self.parsed_dir / f"{document_id}.json"
        cleaned_output_path = self.cleaned_dir / f"{document_id}.txt"
        metadata_output_path = self.metadata_dir / f"{document_id}.json"

        parsed_payload = {
            "document_id": document_id,
            "filename": file_path.name,
            "file_type": parsed.file_type,
            "page_count": parsed.page_count,
            "title": parsed.title,
            "raw_text": parsed.raw_text,
        }

        save_json_file(parsed_output_path, parsed_payload)
        save_text_file(cleaned_output_path, cleaned_text)
        save_json_file(metadata_output_path, metadata.model_dump())

        return DocumentProcessResponse(
            document_id=document_id,
            filename=file_path.name,
            status="success",
            message="Document parsed and preprocessed successfully.",
            parsed_output_path=str(parsed_output_path),
            cleaned_output_path=str(cleaned_output_path),
            metadata_output_path=str(metadata_output_path),
            char_count_raw=len(parsed.raw_text),
            char_count_cleaned=len(cleaned_text),
            page_count=parsed.page_count,
        )