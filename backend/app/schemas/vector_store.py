from typing import Literal

from pydantic import BaseModel


class VectorStoreResponse(BaseModel):
    document_id: str
    status: Literal["success"]
    message: str
    index_name: str
    vector_count: int
    embedding_dimension: int
    manifest_path: str
    stored_document_path: str