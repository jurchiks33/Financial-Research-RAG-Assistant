from pydantic import BaseModel, Field
from typing import List, Optional


class ChatQueryRequest(BaseModel):
    question: str = Field(..., min_length=1)
    document_id: str
    top_k: int = Field(default=5, ge=1, le=10)


class CitationItem(BaseModel):
    index: int
    chunk_id: str
    chunk_index: int
    source_filename: Optional[str] = None
    text: str
    score: float
    char_start: Optional[int] = None
    char_end: Optional[int] = None


class ChatQueryResponse(BaseModel):
    question: str
    answer: str
    citations: List[CitationItem]