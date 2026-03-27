# Phase 3 - Evaluation and Quality

## First milestone
Implement a retrieval benchmark dataset and retrieval evaluation runner.

## Goal
Measure whether the retrieval pipeline returns relevant chunks for known finance/document questions.

## Current benchmark method
For each query:
- retrieve top-k chunks
- compare retrieved chunk text against expected keywords
- calculate score = matched expected keywords / total expected keywords

## Current limitations
- keyword matching is approximate
- not yet using rank-aware metrics
- not yet scoring answer faithfulness or citation correctness

## Future upgrades
- Recall@k
- Precision@k
- MRR
- nDCG
- answer quality evaluation
- citation alignment evaluation