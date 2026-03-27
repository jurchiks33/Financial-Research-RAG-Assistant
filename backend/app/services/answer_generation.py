import os
import re
from typing import Any, List

from openai import OpenAI


class AnswerGenerationService:
    def __init__(self) -> None:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY is not set")

        self.client = OpenAI(api_key=api_key)
        self.model = os.getenv("OPENAI_CHAT_MODEL", "gpt-4.1-mini")

    def _get_field(self, item: Any, field_name: str, default=None):
        if isinstance(item, dict):
            return item.get(field_name, default)
        return getattr(item, field_name, default)

    def _build_context(self, retrieval_results: List[Any]) -> str:
        parts = []

        for idx, item in enumerate(retrieval_results, start=1):
            text = (self._get_field(item, "text", "") or "").strip()
            source_filename = self._get_field(item, "source_filename", "unknown")
            chunk_id = self._get_field(item, "chunk_id", "unknown")
            chunk_index = self._get_field(item, "chunk_index", -1)

            parts.append(
                f"[{idx}] "
                f"source={source_filename} "
                f"chunk_id={chunk_id} "
                f"chunk_index={chunk_index}\n"
                f"{text}"
            )

        return "\n\n".join(parts)

    def generate_answer(self, question: str, retrieval_results: List[Any]) -> str:
        context = self._build_context(retrieval_results)

        system_prompt = """
You are a financial research assistant.

Answer the user's question ONLY using the provided context.
Do not invent facts.
If the answer is not supported by the context, say that the information is not available in the retrieved passages.

Citations rules:
- Use citation markers like [1], [2], [3]
- Every important factual claim must have a citation
- Only cite the chunk numbers provided in context
- Do not cite anything not present in the context
"""

        user_prompt = f"""
Question:
{question}

Context:
{context}

Write a concise answer with inline citations.
"""

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=0.1,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )

        content = response.choices[0].message.content
        return content.strip() if content else ""

    def extract_used_citation_indexes(self, answer: str) -> List[int]:
        matches = re.findall(r"\[(\d+)\]", answer)
        indexes = sorted({int(m) for m in matches})
        return indexes