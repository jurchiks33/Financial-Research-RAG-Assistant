from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from backend.app.schemas.document import DocumentMetadata


def build_document_metadata(
    document_id: str,
    file_path: Path,
    file_type: str,
    file_size: int,
    page_count: Optional[int] = None,
    title: Optional[str] = None,
    uploaded_at: Optional[datetime] = None,
) -> DocumentMetadata:
    return DocumentMetadata(
        document_id=document_id,
        filename=file_path.name,
        original_path=str(file_path),
        file_type=file_type,
        file_size=file_size,
        page_count=page_count,
        title=title,
        uploaded_at=uploaded_at,
        parsed_at=datetime.now(timezone.utc),
    )