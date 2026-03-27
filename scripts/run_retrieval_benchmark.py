import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from backend.app.utils.benchmark_loader import load_retrieval_benchmark_dataset
from backend.app.services.evaluation_service import evaluate_retrieval_dataset


def main():
    dataset_path = "data/benchmarks/retrieval_benchmark.json"
    dataset = load_retrieval_benchmark_dataset(dataset_path)
    summary = evaluate_retrieval_dataset(dataset)

    print("\n=== Retrieval Benchmark Summary ===")
    print(f"Dataset: {summary.dataset_name}")
    print(f"Total cases: {summary.total_cases}")
    print(f"Passed: {summary.passed_cases}")
    print(f"Failed: {summary.failed_cases}")
    print(f"Average score: {summary.average_score:.2f}\n")

    for result in summary.results:
        print(f"[{result.case_id}] {result.query}")
        print(f"  Matched: {result.matched}")
        print(
            f"  Keyword matches: {result.keyword_match_count}/{result.total_expected_keywords}"
        )
        print(f"  Score: {result.score:.2f}")
        print(f"  Retrieved chunk IDs: {result.retrieved_chunk_ids}")
        print()


if __name__ == "__main__":
    main()