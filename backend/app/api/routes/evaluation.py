from fastapi import APIRouter
from backend.app.schemas.common import MessageResponse

router = APIRouter()


@router.get("", response_model=MessageResponse)
def evaluation_placeholder():
    return MessageResponse(message="Evaluation endpoint placeholder")