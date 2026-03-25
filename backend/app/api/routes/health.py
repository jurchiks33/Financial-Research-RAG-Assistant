from fastapi import APIRouter
from backend.app.config import settings
from backend.app.core.constants import APP_VERSION
from backend.app.schemas.common import HealthResponse

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def health_check():
    return HealthResponse(
        status="ok",
        service=settings.APP_NAME,
        environment=settings.APP_ENV,
        version=APP_VERSION,
    )