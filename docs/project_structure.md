# Project Folder Structure

```text
financial-research-rag-assistant/
│
├── README.md
├── .env
├── .env.example
├── .gitignore
├── docker-compose.yml
├── requirements.txt
├── pyproject.toml
│
├── docs/
│   ├── project_overview.md
│   ├── architecture.md
│   ├── api_spec.md
│   ├── evaluation.md
│   ├── setup_guide.md
│   └── screenshots/
│       ├── chat_ui.png
│       ├── upload_page.png
│       └── evaluation_dashboard.png
│
├── data/
│   ├── raw/
│   │   ├── annual_reports/
│   │   ├── earnings_calls/
│   │   ├── macro_reports/
│   │   └── research_notes/
│   │
│   ├── processed/
│   │   ├── parsed_documents/
│   │   ├── cleaned_text/
│   │   ├── chunks/
│   │   └── metadata/
│   │
│   ├── embeddings/
│   │   └── local_cache/
│   │
│   └── evaluation/
│       ├── qa_dataset.json
│       ├── retrieval_benchmark.json
│       └── answer_eval_results.json
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── dependencies.py
│   │   │
│   │   ├── api/
│   │   │   ├── routes/
│   │   │   │   ├── health.py
│   │   │   │   ├── documents.py
│   │   │   │   ├── chat.py
│   │   │   │   ├── retrieval.py
│   │   │   │   ├── evaluation.py
│   │   │   │   └── admin.py
│   │   │   │
│   │   │   └── router.py
│   │   │
│   │   ├── core/
│   │   │   ├── logging.py
│   │   │   ├── security.py
│   │   │   ├── exceptions.py
│   │   │   └── constants.py
│   │   │
│   │   ├── models/
│   │   │   ├── document.py
│   │   │   ├── chunk.py
│   │   │   ├── query.py
│   │   │   ├── answer.py
│   │   │   ├── evaluation.py
│   │   │   └── user_feedback.py
│   │   │
│   │   ├── schemas/
│   │   │   ├── document.py
│   │   │   ├── chat.py
│   │   │   ├── retrieval.py
│   │   │   ├── evaluation.py
│   │   │   └── common.py
│   │   │
│   │   ├── services/
│   │   │   ├── ingestion_service.py
│   │   │   ├── parser_service.py
│   │   │   ├── chunking_service.py
│   │   │   ├── embedding_service.py
│   │   │   ├── vector_store_service.py
│   │   │   ├── retrieval_service.py
│   │   │   ├── reranker_service.py
│   │   │   ├── generation_service.py
│   │   │   ├── citation_service.py
│   │   │   ├── evaluation_service.py
│   │   │   ├── feedback_service.py
│   │   │   └── document_classifier_service.py
│   │   │
│   │   ├── repositories/
│   │   │   ├── document_repository.py
│   │   │   ├── chunk_repository.py
│   │   │   ├── evaluation_repository.py
│   │   │   └── feedback_repository.py
│   │   │
│   │   ├── db/
│   │   │   ├── session.py
│   │   │   ├── base.py
│   │   │   └── init_db.py
│   │   │
│   │   ├── rag/
│   │   │   ├── pipeline.py
│   │   │   ├── prompts.py
│   │   │   ├── retriever.py
│   │   │   ├── reranker.py
│   │   │   ├── generator.py
│   │   │   ├── citation_builder.py
│   │   │   └── guards.py
│   │   │
│   │   ├── utils/
│   │   │   ├── file_loader.py
│   │   │   ├── text_cleaner.py
│   │   │   ├── metadata_extractor.py
│   │   │   ├── pdf_helpers.py
│   │   │   ├── token_counter.py
│   │   │   └── time_utils.py
│   │   │
│   │   └── tests/
│   │       ├── test_health.py
│   │       ├── test_ingestion.py
│   │       ├── test_chunking.py
│   │       ├── test_embeddings.py
│   │       ├── test_retrieval.py
│   │       ├── test_generation.py
│   │       └── test_evaluation.py
│   │
│   ├── migrations/
│   │   ├── env.py
│   │   └── versions/
│   │
│   └── scripts/
│       ├── ingest_documents.py
│       ├── rebuild_index.py
│       ├── run_evaluation.py
│       ├── seed_sample_data.py
│       └── export_metrics.py
│
├── frontend/
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   │
│   ├── public/
│   │   └── favicon.ico
│   │
│   └── src/
│       ├── main.tsx
│       ├── App.tsx
│       ├── index.css
│       │
│       ├── assets/
│       │   └── logo.svg
│       │
│       ├── components/
│       │   ├── chat/
│       │   │   ├── ChatWindow.tsx
│       │   │   ├── MessageList.tsx
│       │   │   ├── MessageInput.tsx
│       │   │   ├── AnswerCard.tsx
│       │   │   └── CitationList.tsx
│       │   │
│       │   ├── documents/
│       │   │   ├── UploadPanel.tsx
│       │   │   ├── DocumentTable.tsx
│       │   │   ├── DocumentFilters.tsx
│       │   │   └── DocumentDetailsDrawer.tsx
│       │   │
│       │   ├── evaluation/
│       │   │   ├── EvaluationDashboard.tsx
│       │   │   ├── RetrievalMetricsCard.tsx
│       │   │   ├── AnswerQualityCard.tsx
│       │   │   └── FeedbackSummary.tsx
│       │   │
│       │   ├── layout/
│       │   │   ├── Navbar.tsx
│       │   │   ├── Sidebar.tsx
│       │   │   ├── PageContainer.tsx
│       │   │   └── Header.tsx
│       │   │
│       │   └── common/
│       │       ├── Button.tsx
│       │       ├── Card.tsx
│       │       ├── Spinner.tsx
│       │       ├── EmptyState.tsx
│       │       └── Badge.tsx
│       │
│       ├── pages/
│       │   ├── ChatPage.tsx
│       │   ├── DocumentsPage.tsx
│       │   ├── EvaluationPage.tsx
│       │   ├── AdminPage.tsx
│       │   └── NotFoundPage.tsx
│       │
│       ├── services/
│       │   ├── api.ts
│       │   ├── chatService.ts
│       │   ├── documentService.ts
│       │   ├── retrievalService.ts
│       │   └── evaluationService.ts
│       │
│       ├── hooks/
│       │   ├── useChat.ts
│       │   ├── useDocuments.ts
│       │   ├── useEvaluation.ts
│       │   └── useUpload.ts
│       │
│       ├── types/
│       │   ├── chat.ts
│       │   ├── document.ts
│       │   ├── retrieval.ts
│       │   └── evaluation.ts
│       │
│       ├── utils/
│       │   ├── formatters.ts
│       │   ├── constants.ts
│       │   └── helpers.ts
│       │
│       └── router/
│           └── index.tsx
│
├── vector_store/
│   ├── qdrant/
│   │   └── collections/
│   └── pgvector/
│       └── init.sql
│
├── notebooks/
│   ├── 01_document_parsing_experiments.ipynb
│   ├── 02_chunking_experiments.ipynb
│   ├── 03_embedding_comparison.ipynb
│   ├── 04_retrieval_tests.ipynb
│   └── 05_evaluation_analysis.ipynb
│
├── experiments/
│   ├── prompt_versions/
│   │   ├── v1.md
│   │   ├── v2.md
│   │   └── v3.md
│   │
│   ├── retrieval_configs/
│   │   ├── baseline.yaml
│   │   ├── hybrid.yaml
│   │   └── rerank.yaml
│   │
│   └── results/
│       ├── retrieval/
│       ├── generation/
│       └── latency/
│
└── deployment/
    ├── backend.Dockerfile
    ├── frontend.Dockerfile
    ├── nginx.conf
    ├── render.yaml
    ├── railway.json
    └── github_actions/
        └── ci.yml
``` 