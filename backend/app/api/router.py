from fastapi import APIRouter

from backend.app.api.routes.health import router as health_router
from backend.app.api.routes.documents import router as documents_router
from backend.app.api.routes.chat import router as chat_router
from backend.app.api.routes.retrieval import router as retrieval_router
from backend.app.api.routes.evaluation import router as evaluation_router
from backend.app.api.routes.admin import router as admin_router

api_router = APIRouter()

api_router.include_router(health_router, prefix="", tags=["Health"])
api_router.include_router(documents_router, prefix="/documents", tags=["Documents"])
api_router.include_router(chat_router, prefix="/chat", tags=["Chat"])
api_router.include_router(retrieval_router, prefix="/retrieval", tags=["Retrieval"])
api_router.include_router(evaluation_router, prefix="/evaluation", tags=["Evaluation"])
api_router.include_router(admin_router, prefix="/admin", tags=["Admin"])