from fastapi import APIRouter
from backend.app.schemas.common import MessageResponse

router = APIRouter()


@router.get("", response_model=MessageResponse)
def retrieval_placeholder():
    return MessageResponse(message="Retrieval endpoint placeholder")