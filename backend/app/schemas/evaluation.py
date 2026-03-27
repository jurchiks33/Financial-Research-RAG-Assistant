from pydantic import BaseModel, Field
from typing import List, Optional


class RetrievalBenchmarkCase(BaseModel):
    id: str
    document_id: str
    source_filename: Optional[str] = None
    query: str
    expected_chunk_keywords: List[str] = Field(default_factory=list)
    expected_chunk_ids: List[str] = Field(default_factory=list)
    top_k: int = 5
    notes: Optional[str] = None


class RetrievalBenchmarkDataset(BaseModel):
    dataset_name: str
    description: Optional[str] = None
    cases: List[RetrievalBenchmarkCase]


class RetrievalCaseResult(BaseModel):
    case_id: str
    query: str
    top_k: int
    matched: bool
    keyword_match_count: int
    total_expected_keywords: int
    matched_chunk_ids: List[str] = Field(default_factory=list)
    retrieved_chunk_ids: List[str] = Field(default_factory=list)
    retrieved_texts: List[str] = Field(default_factory=list)
    score: float
    notes: Optional[str] = None


class RetrievalBenchmarkSummary(BaseModel):
    dataset_name: str
    total_cases: int
    passed_cases: int
    failed_cases: int
    average_score: float
    results: List[RetrievalCaseResult]