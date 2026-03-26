from pathlib import Path

from fastapi import APIRouter, File, HTTPException, UploadFile, status

from backend.app.schemas.chunk import ChunkResponse
from backend.app.schemas.common import MessageResponse
from backend.app.schemas.document import (
    DocumentProcessResponse,
    DocumentUploadResponse,
)
from backend.app.schemas.embedding import EmbeddingResponse
from backend.app.schemas.vector_store import VectorStoreResponse
from backend.app.services.chunking_service import ChunkingService
from backend.app.services.embedding_service import EmbeddingService
from backend.app.services.ingestion_service import IngestionService
from backend.app.services.storage_service import (
    FileValidationError,
    LocalStorageService,
)
from backend.app.services.vector_store_service import VectorStoreService

router = APIRouter()
storage_service = LocalStorageService()
ingestion_service = IngestionService()
chunking_service = ChunkingService()
embedding_service = EmbeddingService()
vector_store_service = VectorStoreService()


@router.get("", response_model=MessageResponse)
def list_documents():
    uploads_dir = Path("data/uploads")
    uploads_dir.mkdir(parents=True, exist_ok=True)

    files = [p.name for p in uploads_dir.iterdir() if p.is_file()]

    return MessageResponse(
        message=f"Found {len(files)} uploaded document(s): {files}"
    )


@router.post(
    "/upload",
    response_model=DocumentUploadResponse,
    status_code=status.HTTP_201_CREATED,
)
async def upload_document(file: UploadFile = File(...)) -> DocumentUploadResponse:
    try:
        result = await storage_service.save_upload(file)
        return DocumentUploadResponse(**result)
    except FileValidationError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to upload document.",
        ) from exc


@router.post(
    "/{filename}/process",
    response_model=DocumentProcessResponse,
    status_code=status.HTTP_200_OK,
)
def process_document(filename: str) -> DocumentProcessResponse:
    try:
        return ingestion_service.process_uploaded_document(filename)
    except FileNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Processing failed: {exc}",
        ) from exc


@router.post(
    "/{document_id}/chunk",
    response_model=ChunkResponse,
    status_code=status.HTTP_200_OK,
)
def chunk_document(document_id: str) -> ChunkResponse:
    try:
        return chunking_service.chunk_document(document_id=document_id)
    except FileNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Chunking failed: {exc}",
        ) from exc


@router.post(
    "/{document_id}/embed",
    response_model=EmbeddingResponse,
    status_code=status.HTTP_200_OK,
)
def embed_document(document_id: str) -> EmbeddingResponse:
    try:
        return embedding_service.embed_document(document_id=document_id)
    except FileNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Embedding generation failed: {exc}",
        ) from exc


@router.post(
    "/{document_id}/store-vectors",
    response_model=VectorStoreResponse,
    status_code=status.HTTP_200_OK,
)
def store_document_vectors(document_id: str) -> VectorStoreResponse:
    try:
        return vector_store_service.store_document_vectors(document_id=document_id)
    except FileNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Vector storage failed: {exc}",
        ) from exc