from datetime import datetime
from typing import Literal, Optional

from pydantic import BaseModel


class DocumentUploadResponse(BaseModel):
    document_id: str
    filename: str
    content_type: str
    size_bytes: int
    stored_path: str
    status: Literal["uploaded"]


class DocumentMetadata(BaseModel):
    document_id: str
    filename: str
    original_path: str
    file_type: str
    file_size: int
    page_count: Optional[int] = None
    title: Optional[str] = None
    uploaded_at: Optional[datetime] = None
    parsed_at: datetime
    preprocessing_version: str = "v1"


class DocumentProcessResponse(BaseModel):
    document_id: str
    filename: str
    status: Literal["success"]
    message: str
    parsed_output_path: str
    cleaned_output_path: str
    metadata_output_path: str
    char_count_raw: int
    char_count_cleaned: int
    page_count: Optional[int] = None