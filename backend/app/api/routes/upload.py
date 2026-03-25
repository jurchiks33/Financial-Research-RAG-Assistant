from fastapi import APIRouter, File, HTTPException, UploadFile, status

from backend.app.schemas.document import DocumentUploadResponse
from backend.app.services.storage_service import (
    FileValidationError,
    LocalStorageService,
)

router = APIRouter(prefix="/documents", tags=["documents"])
storage_service = LocalStorageService()


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