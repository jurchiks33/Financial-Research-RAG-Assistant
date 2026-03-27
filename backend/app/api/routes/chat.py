from inspect import signature

from fastapi import APIRouter, HTTPException

from backend.app.schemas.common import MessageResponse
from backend.app.schemas.chat import (
    ChatQueryRequest,
    ChatQueryResponse,
    CitationItem,
)
from backend.app.services.answer_generation import AnswerGenerationService
from backend.app.services.retrieval_service import RetrievalService

router = APIRouter()

_answer_service = None
_retrieval_service = None


def get_answer_service() -> AnswerGenerationService:
    global _answer_service
    if _answer_service is None:
        _answer_service = AnswerGenerationService()
    return _answer_service


def get_retrieval_service() -> RetrievalService:
    global _retrieval_service
    if _retrieval_service is None:
        _retrieval_service = RetrievalService()
    return _retrieval_service


def get_field(item, field_name, default=None):
    if isinstance(item, dict):
        return item.get(field_name, default)
    return getattr(item, field_name, default)


def normalize_retrieval_results(results):
    if results is None:
        return []

    if isinstance(results, dict):
        return results.get("results", [])

    if hasattr(results, "results"):
        return getattr(results, "results", [])

    if isinstance(results, list):
        return results

    return []


def filter_results_by_document_id(results, document_id):
    if not document_id:
        return results

    filtered = [
        item for item in results
        if get_field(item, "document_id") == document_id
    ]
    return filtered


def run_retrieval(retrieval_service: RetrievalService, payload: ChatQueryRequest):
    method = None

    if hasattr(retrieval_service, "search"):
        method = retrieval_service.search
    elif hasattr(retrieval_service, "retrieve"):
        method = retrieval_service.retrieve
    else:
        raise RuntimeError(
            "RetrievalService does not expose search(...) or retrieve(...)."
        )

    method_signature = signature(method)
    accepted_params = method_signature.parameters.keys()

    kwargs = {}

    if "query" in accepted_params:
        kwargs["query"] = payload.question
    elif "question" in accepted_params:
        kwargs["question"] = payload.question
    else:
        raise RuntimeError(
            "RetrievalService method must accept either 'query' or 'question'."
        )

    if "top_k" in accepted_params:
        kwargs["top_k"] = payload.top_k
    elif "k" in accepted_params:
        kwargs["k"] = payload.top_k

    if "document_id" in accepted_params and payload.document_id:
        kwargs["document_id"] = payload.document_id

    raw_results = method(**kwargs)
    results = normalize_retrieval_results(raw_results)

    if "document_id" not in accepted_params and payload.document_id:
        results = filter_results_by_document_id(results, payload.document_id)

    return results


@router.get("", response_model=MessageResponse)
def chat_placeholder():
    return MessageResponse(message="Chat endpoint placeholder")


@router.post("/query", response_model=ChatQueryResponse)
def query_with_citations(payload: ChatQueryRequest):
    try:
        retrieval_service = get_retrieval_service()
        retrieval_results = run_retrieval(retrieval_service, payload)

        if not retrieval_results:
            return ChatQueryResponse(
                question=payload.question,
                answer="No relevant context was found for this question.",
                citations=[],
            )

        answer_service = get_answer_service()

        answer = answer_service.generate_answer(
            question=payload.question,
            retrieval_results=retrieval_results,
        )

        used_indexes = answer_service.extract_used_citation_indexes(answer)

        citations = []
        for idx in used_indexes:
            if 1 <= idx <= len(retrieval_results):
                item = retrieval_results[idx - 1]
                citations.append(
                    CitationItem(
                        index=idx,
                        chunk_id=get_field(item, "chunk_id"),
                        chunk_index=get_field(item, "chunk_index"),
                        source_filename=get_field(item, "source_filename"),
                        text=get_field(item, "text"),
                        score=get_field(item, "score"),
                        char_start=get_field(item, "char_start"),
                        char_end=get_field(item, "char_end"),
                    )
                )

        return ChatQueryResponse(
            question=payload.question,
            answer=answer,
            citations=citations,
        )

    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))