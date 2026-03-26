from fastapi import APIRouter, HTTPException, status

from backend.app.schemas.retrieval import RetrievalRequest, RetrievalResponse
from backend.app.services.retrieval_service import RetrievalService

router = APIRouter()
retrieval_service = RetrievalService()


@router.post("", response_model=RetrievalResponse, status_code=status.HTTP_200_OK)
def retrieve_chunks(payload: RetrievalRequest) -> RetrievalResponse:
    try:
        return retrieval_service.retrieve(
            query=payload.query,
            top_k=payload.top_k,
        )
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
            detail=f"Retrieval failed: {exc}",
        ) from exc
