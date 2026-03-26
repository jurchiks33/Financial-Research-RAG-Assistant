from pathlib import Path
from typing import Optional

from pypdf import PdfReader

from backend.app.utils.file_loader import get_file_extension, validate_supported_file


class ParsedDocument:
    def __init__(
        self,
        raw_text: str,
        file_type: str,
        page_count: Optional[int] = None,
        title: Optional[str] = None,
    ):
        self.raw_text = raw_text
        self.file_type = file_type
        self.page_count = page_count
        self.title = title


class ParserService:
    def parse(self, file_path: Path) -> ParsedDocument:
        validate_supported_file(file_path)
        extension = get_file_extension(file_path)

        if extension == ".pdf":
            return self._parse_pdf(file_path)
        if extension in {".txt", ".md"}:
            return self._parse_text_file(file_path)

        raise ValueError(f"Unsupported file extension: {extension}")

    def _parse_pdf(self, file_path: Path) -> ParsedDocument:
        reader = PdfReader(str(file_path))
        pages = []
        title = None

        try:
            if reader.metadata:
                title = reader.metadata.title
        except Exception:
            title = None

        for page in reader.pages:
            page_text = page.extract_text() or ""
            pages.append(page_text)

        raw_text = "\n\n".join(pages).strip()

        return ParsedDocument(
            raw_text=raw_text,
            file_type="pdf",
            page_count=len(reader.pages),
            title=title,
        )

    def _parse_text_file(self, file_path: Path) -> ParsedDocument:
        raw_text = file_path.read_text(encoding="utf-8", errors="ignore")

        extension = get_file_extension(file_path)
        file_type = extension.replace(".", "")

        return ParsedDocument(
            raw_text=raw_text.strip(),
            file_type=file_type,
            page_count=None,
            title=file_path.stem,
        )