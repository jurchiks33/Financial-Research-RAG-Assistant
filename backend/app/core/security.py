from backend.app.config import settings


def get_secret_key() -> str:
    return settings.SECRET_KEY