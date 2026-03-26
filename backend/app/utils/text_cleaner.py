import re
import unicodedata


def normalize_unicode(text: str) -> str:
    if not text:
        return ""
    return unicodedata.normalize("NFKC", text)


def remove_null_bytes(text: str) -> str:
    return text.replace("\x00", "")


def normalize_line_endings(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def collapse_excess_whitespace(text: str) -> str:
    lines = [re.sub(r"[ \t]+", " ", line).strip() for line in text.split("\n")]

    cleaned_lines = []
    blank_streak = 0

    for line in lines:
        if line == "":
            blank_streak += 1
            if blank_streak <= 1:
                cleaned_lines.append("")
        else:
            blank_streak = 0
            cleaned_lines.append(line)

    return "\n".join(cleaned_lines).strip()


def fix_hyphenated_line_breaks(text: str) -> str:
    # joins words split like:
    # finan-
    # cial  -> financial
    return re.sub(r"(\w)-\n(\w)", r"\1\2", text)


def join_single_newlines_inside_paragraphs(text: str) -> str:
    # preserve paragraph breaks, but join wrapped lines
    text = re.sub(r"(?<!\n)\n(?!\n)", " ", text)
    return text


def preprocess_text(text: str) -> str:
    text = remove_null_bytes(text)
    text = normalize_unicode(text)
    text = normalize_line_endings(text)
    text = fix_hyphenated_line_breaks(text)
    text = join_single_newlines_inside_paragraphs(text)
    text = collapse_excess_whitespace(text)
    return text