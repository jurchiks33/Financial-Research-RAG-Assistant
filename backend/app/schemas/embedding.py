from typing import Literal

from pydantic import BaseModel


class EmbeddingResponse(BaseModel):
    document_id: str
    status: Literal["success"]
    message: str
    model_name: str
    embedding_count: int
    embedding_dimension: int
    embeddings_output_path: str
    metadata_output_path: str