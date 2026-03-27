import json
from pathlib import Path

from backend.app.schemas.evaluation import RetrievalBenchmarkDataset


def load_retrieval_benchmark_dataset(path: str) -> RetrievalBenchmarkDataset:
    dataset_path = Path(path)
    if not dataset_path.exists():
        raise FileNotFoundError(f"Benchmark dataset not found: {path}")

    with open(dataset_path, "r", encoding="utf-8") as f:
        raw_data = json.load(f)

    return RetrievalBenchmarkDataset(**raw_data)