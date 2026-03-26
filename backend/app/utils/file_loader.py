import json
from pathlib import Path
from typing import Any


SUPPORTED_EXTENSIONS = {".pdf", ".txt", ".md"}


def ensure_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def get_file_extension(file_path: Path) -> str:
    return file_path.suffix.lower()


def validate_supported_file(file_path: Path) -> None:
    ext = get_file_extension(file_path)
    if ext not in SUPPORTED_EXTENSIONS:
        raise ValueError(
            f"Unsupported file type: {ext}. Supported types: {sorted(SUPPORTED_EXTENSIONS)}"
        )


def save_text_file(path: Path, content: str) -> None:
    ensure_directory(path.parent)
    path.write_text(content, encoding="utf-8")


def save_json_file(path: Path, payload: Any) -> None:
    ensure_directory(path.parent)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False, default=str), encoding="utf-8")