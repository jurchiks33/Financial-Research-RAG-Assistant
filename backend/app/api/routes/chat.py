from fastapi import APIRouter
from backend.app.schemas.common import MessageResponse

router = APIRouter()


@router.get("", response_model=MessageResponse)
def chat_placeholder():
    return MessageResponse(message="Chat endpoint placeholder")