from typing import List

from backend.app.schemas.evaluation import (
    RetrievalBenchmarkCase,
    RetrievalBenchmarkDataset,
    RetrievalCaseResult,
    RetrievalBenchmarkSummary,
)
from backend.app.services.retrieval_service import RetrievalService


retrieval_service = RetrievalService()


def evaluate_retrieval_case(case: RetrievalBenchmarkCase) -> RetrievalCaseResult:
    response = retrieval_service.retrieve(
        query=case.query,
        top_k=case.top_k,
    )

    retrieved_chunks = response.results
    retrieved_texts = [chunk.text for chunk in retrieved_chunks]
    retrieved_chunk_ids = [chunk.chunk_id for chunk in retrieved_chunks]

    matched_keywords = 0
    lowered_texts = [text.lower() for text in retrieved_texts]

    for keyword in case.expected_chunk_keywords:
        keyword_lower = keyword.lower()
        if any(keyword_lower in text for text in lowered_texts):
            matched_keywords += 1

    total_keywords = len(case.expected_chunk_keywords)
    score = matched_keywords / total_keywords if total_keywords > 0 else 0.0
    matched = score > 0

    matched_chunk_ids = []
    if case.expected_chunk_ids:
        matched_chunk_ids = [
            chunk_id for chunk_id in retrieved_chunk_ids
            if chunk_id in case.expected_chunk_ids
        ]

    return RetrievalCaseResult(
        case_id=case.id,
        query=case.query,
        top_k=case.top_k,
        matched=matched,
        keyword_match_count=matched_keywords,
        total_expected_keywords=total_keywords,
        matched_chunk_ids=matched_chunk_ids,
        retrieved_chunk_ids=retrieved_chunk_ids,
        retrieved_texts=retrieved_texts,
        score=score,
        notes=case.notes,
    )


def evaluate_retrieval_dataset(
    dataset: RetrievalBenchmarkDataset,
) -> RetrievalBenchmarkSummary:
    results: List[RetrievalCaseResult] = []

    for case in dataset.cases:
        result = evaluate_retrieval_case(case)
        results.append(result)

    total_cases = len(results)
    passed_cases = sum(1 for r in results if r.matched)
    failed_cases = total_cases - passed_cases
    average_score = (
        sum(r.score for r in results) / total_cases if total_cases > 0 else 0.0
    )

    return RetrievalBenchmarkSummary(
        dataset_name=dataset.dataset_name,
        total_cases=total_cases,
        passed_cases=passed_cases,
        failed_cases=failed_cases,
        average_score=average_score,
        results=results,
    )