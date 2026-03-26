from typing import List

from pydantic import BaseModel, Field


class RetrievalRequest(BaseModel):
    query: str = Field(..., min_length=1)
    top_k: int = Field(default=5, ge=1, le=20)


class RetrievedChunk(BaseModel):
    document_id: str
    chunk_id: str
    chunk_index: int
    source_filename: str
    score: float
    char_start: int
    char_end: int
    token_estimate: int | None = None
    text: str


class RetrievalResponse(BaseModel):
    query: str
    top_k: int
    result_count: int
    results: List[RetrievedChunk]