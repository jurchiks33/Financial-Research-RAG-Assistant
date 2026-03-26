from typing import Optional

from pydantic import BaseModel


class ChunkMetadata(BaseModel):
    chunk_id: str
    document_id: str
    source_filename: str
    chunk_index: int
    char_start: int
    char_end: int
    chunk_size: int
    overlap: int
    token_estimate: Optional[int] = None


class ChunkResponse(BaseModel):
    document_id: str
    source_filename: str
    status: str
    message: str
    chunk_count: int
    output_path: str
    chunk_size: int
    chunk_overlap: int