

# Project Structure Explained

This document explains the purpose of each major folder and the role of the most important files in the **Financial Research RAG Assistant** project.

---

## Root Files

### `README.md`
Main project entry point.  
Explains what the project does, key features, how to run it, and where to find more detailed documentation.

### `.env`
Stores local environment variables such as API keys, database URLs, model settings, and application secrets.

### `.env.example`
Template showing which environment variables are required to run the project.

### `.gitignore`
Defines which files and folders Git should ignore, such as virtual environments, cache files, and secrets.

### `docker-compose.yml`
Starts the main project services together, such as backend, frontend, database, and vector store.

### `requirements.txt`
Lists Python packages required by the backend.

### `pyproject.toml`
Stores Python project configuration and dependency/tooling settings.

---

## `docs/`

Contains all project documentation.

### `docs/project_overview.md`
High-level explanation of the project, its goals, features, and use case.

### `docs/project_structure.md`
Displays the folder and file structure of the project.

### `docs/project_structure_explained.md`
Explains what each important folder and file does.

### `docs/architecture.md`
Describes how the system works end-to-end, including ingestion, embeddings, retrieval, answer generation, and evaluation.

### `docs/api_spec.md`
Documents backend API endpoints, request formats, and responses.

### `docs/evaluation.md`
Explains how retrieval and answer quality are measured.

### `docs/setup_guide.md`
Step-by-step instructions for local installation and running the project.

### `docs/screenshots/`
Stores screenshots used in documentation, such as the chat interface, upload screen, and evaluation dashboard.

---

## `data/`

Stores project data in different processing stages.

### `data/raw/`
Contains original source files before any processing.

- `annual_reports/` — company annual reports
- `earnings_calls/` — earnings call transcripts
- `macro_reports/` — macroeconomic reports
- `research_notes/` — analyst notes or research material

### `data/processed/`
Contains intermediate outputs generated during preprocessing.

- `parsed_documents/` — text extracted from source files
- `cleaned_text/` — normalized and cleaned text
- `chunks/` — document chunks created for retrieval
- `metadata/` — metadata associated with documents and chunks

### `data/embeddings/`
Stores local embedding cache or exported vector representations if needed.

### `data/evaluation/`
Stores benchmark and evaluation files.

- `qa_dataset.json` — question-answer evaluation dataset
- `retrieval_benchmark.json` — retrieval relevance test data
- `answer_eval_results.json` — recorded answer evaluation results

---

## `backend/`

Contains the FastAPI backend, retrieval pipeline, database logic, and evaluation logic.

### `backend/app/main.py`
Main backend entry point. Starts the FastAPI application and registers routes.

### `backend/app/config.py`
Loads configuration values such as environment variables, model names, and service URLs.

### `backend/app/dependencies.py`
Defines shared FastAPI dependencies used across routes.

---

## `backend/app/api/`

Contains API route definitions.

### `routes/health.py`
Health-check endpoint to confirm the application is running.

### `routes/documents.py`
Endpoints for uploading, listing, and managing documents.

### `routes/chat.py`
Endpoints for asking questions and receiving grounded answers.

### `routes/retrieval.py`
Endpoints for inspecting retrieval results and debugging document matches.

### `routes/evaluation.py`
Endpoints for running or viewing evaluation results.

### `routes/admin.py`
Administrative endpoints for internal tasks and maintenance.

### `router.py`
Combines all route modules into a single API router.

---

## `backend/app/core/`

Contains application-wide core utilities.

### `logging.py`
Centralized logging setup for backend events and debugging.

### `security.py`
Authentication, authorization, and security-related helpers.

### `exceptions.py`
Custom exception classes and shared error handling logic.

### `constants.py`
Application constants used across the backend.

---

## `backend/app/models/`

Defines internal domain or database models.

### `document.py`
Represents a source document stored in the system.

### `chunk.py`
Represents a chunk of text created from a document.

### `query.py`
Represents a user query or retrieval request.

### `answer.py`
Represents a generated answer and related metadata.

### `evaluation.py`
Represents evaluation runs or stored evaluation metrics.

### `user_feedback.py`
Represents user feedback such as helpful/not helpful responses.

---

## `backend/app/schemas/`

Defines request and response schemas for API validation.

### `document.py`
Schemas related to document upload, metadata, and listing.

### `chat.py`
Schemas for chat requests and answers.

### `retrieval.py`
Schemas for retrieval inspection and search results.

### `evaluation.py`
Schemas for evaluation requests and metric responses.

### `common.py`
Shared schema objects used in multiple places.

---

## `backend/app/services/`

Contains the main business logic of the project.

### `ingestion_service.py`
Coordinates document ingestion from upload to storage.

### `parser_service.py`
Extracts text from files such as PDF, DOCX, or TXT.

### `chunking_service.py`
Splits documents into chunks suitable for retrieval.

### `embedding_service.py`
Generates embeddings for document chunks and queries.

### `vector_store_service.py`
Handles storing and retrieving vectors from the vector database.

### `retrieval_service.py`
Finds the most relevant chunks for a user query.

### `reranker_service.py`
Improves ranking of retrieved chunks before answer generation.

### `generation_service.py`
Builds prompts and generates answers from retrieved context.

### `citation_service.py`
Builds citations and source references shown to the user.

### `evaluation_service.py`
Runs retrieval and answer quality benchmarks.

### `feedback_service.py`
Stores and processes user feedback.

### `document_classifier_service.py`
Classifies uploaded documents by type or category.

---

## `backend/app/repositories/`

Handles direct data access and database interaction.

### `document_repository.py`
Reads and writes document records.

### `chunk_repository.py`
Reads and writes chunk records.

### `evaluation_repository.py`
Stores and retrieves evaluation results.

### `feedback_repository.py`
Stores and retrieves user feedback.

---

## `backend/app/db/`

Database connection and initialization files.

### `session.py`
Creates database sessions and connection handling.

### `base.py`
Defines the shared database base model.

### `init_db.py`
Initializes database tables or startup database setup.

---

## `backend/app/rag/`

Contains the main Retrieval-Augmented Generation pipeline logic.

### `pipeline.py`
Coordinates the full RAG flow from query to final answer.

### `prompts.py`
Stores prompt templates used for answer generation.

### `retriever.py`
Implements retrieval logic over indexed chunks.

### `reranker.py`
Implements reranking logic for better result ordering.

### `generator.py`
Wraps model-based answer generation.

### `citation_builder.py`
Builds structured citations from retrieved chunks.

### `guards.py`
Implements safety rules and grounding checks to reduce hallucinations.

---

## `backend/app/utils/`

Small helper functions used across the backend.

### `file_loader.py`
Loads input files from disk or upload locations.

### `text_cleaner.py`
Cleans extracted text before chunking.

### `metadata_extractor.py`
Extracts metadata such as document type, title, company, or year.

### `pdf_helpers.py`
PDF-specific helper logic.

### `token_counter.py`
Counts tokens for prompts, chunks, or limits.

### `time_utils.py`
Date and time helper functions.

---

## `backend/app/tests/`

Automated backend tests.

### `test_health.py`
Tests health-check functionality.

### `test_ingestion.py`
Tests document ingestion flow.

### `test_chunking.py`
Tests chunk generation logic.

### `test_embeddings.py`
Tests embedding creation logic.

### `test_retrieval.py`
Tests retrieval quality and correctness.

### `test_generation.py`
Tests answer generation flow.

### `test_evaluation.py`
Tests evaluation logic and metrics.

---

## `backend/migrations/`

Database migration files used to evolve the database schema over time.

### `env.py`
Migration environment configuration.

### `versions/`
Stores individual migration versions.

---

## `backend/scripts/`

Utility scripts for manual or batch operations.

### `ingest_documents.py`
Runs ingestion on a batch of documents.

### `rebuild_index.py`
Recreates embeddings or vector indexes after document changes.

### `run_evaluation.py`
Runs evaluation benchmarks.

### `seed_sample_data.py`
Adds sample documents or records for testing.

### `export_metrics.py`
Exports evaluation or usage metrics.

---

## `frontend/`

Contains the React frontend application.

### `package.json`
Frontend dependencies and scripts.

### `tsconfig.json`
TypeScript configuration.

### `vite.config.ts`
Vite build and development server configuration.

### `public/favicon.ico`
Browser tab icon.

---

## `frontend/src/`

Main frontend source code.

### `main.tsx`
Frontend entry point.

### `App.tsx`
Top-level application component.

### `index.css`
Global styles.

---

## `frontend/src/assets/`

Stores static frontend assets such as logos.

### `logo.svg`
Project logo.

---

## `frontend/src/components/`

Reusable UI components grouped by purpose.

### `components/chat/`
Components for the chat interface.

- `ChatWindow.tsx` — main chat area
- `MessageList.tsx` — displays conversation history
- `MessageInput.tsx` — question input box
- `AnswerCard.tsx` — shows generated answer
- `CitationList.tsx` — shows source citations

### `components/documents/`
Components for document management.

- `UploadPanel.tsx` — upload area for new documents
- `DocumentTable.tsx` — list of stored documents
- `DocumentFilters.tsx` — filtering controls
- `DocumentDetailsDrawer.tsx` — detailed document info panel

### `components/evaluation/`
Components for evaluation metrics and dashboards.

- `EvaluationDashboard.tsx` — main evaluation screen
- `RetrievalMetricsCard.tsx` — retrieval performance summary
- `AnswerQualityCard.tsx` — answer quality summary
- `FeedbackSummary.tsx` — user feedback overview

### `components/layout/`
Shared layout elements.

- `Navbar.tsx` — top navigation
- `Sidebar.tsx` — side navigation menu
- `PageContainer.tsx` — shared page layout wrapper
- `Header.tsx` — page header section

### `components/common/`
Reusable shared UI elements.

- `Button.tsx`
- `Card.tsx`
- `Spinner.tsx`
- `EmptyState.tsx`
- `Badge.tsx`

---

## `frontend/src/pages/`

Top-level application pages.

### `ChatPage.tsx`
Main question-answering page.

### `DocumentsPage.tsx`
Document upload and management page.

### `EvaluationPage.tsx`
Page showing retrieval and answer evaluation results.

### `AdminPage.tsx`
Administrative page for internal controls.

### `NotFoundPage.tsx`
Fallback page for invalid routes.

---

## `frontend/src/services/`

Frontend API communication layer.

### `api.ts`
Base API client configuration.

### `chatService.ts`
Calls backend chat endpoints.

### `documentService.ts`
Calls backend document endpoints.

### `retrievalService.ts`
Calls retrieval inspection endpoints.

### `evaluationService.ts`
Calls evaluation endpoints.

---

## `frontend/src/hooks/`

Reusable React hooks for state and data handling.

### `useChat.ts`
Manages chat logic and state.

### `useDocuments.ts`
Manages document listing and document state.

### `useEvaluation.ts`
Manages evaluation data loading.

### `useUpload.ts`
Handles upload logic and file submission state.

---

## `frontend/src/types/`

TypeScript type definitions.

### `chat.ts`
Chat-related types.

### `document.ts`
Document-related types.

### `retrieval.ts`
Retrieval-related types.

### `evaluation.ts`
Evaluation-related types.

---

## `frontend/src/utils/`

Frontend helper functions and constants.

### `formatters.ts`
Formatting helpers for dates, labels, and display values.

### `constants.ts`
Shared frontend constants.

### `helpers.ts`
General helper functions.

---

## `frontend/src/router/`

Routing setup.

### `index.tsx`
Defines frontend application routes.

---

## `vector_store/`

Contains vector database related setup.

### `vector_store/qdrant/`
Configuration or local data for Qdrant.

### `vector_store/qdrant/collections/`
Qdrant collection-related files.

### `vector_store/pgvector/init.sql`
Initialization SQL for pgvector setup.

---

## `notebooks/`

Research and experiment notebooks used during development.

### `01_document_parsing_experiments.ipynb`
Tests document extraction quality.

### `02_chunking_experiments.ipynb`
Tests chunking strategies.

### `03_embedding_comparison.ipynb`
Compares embedding models or approaches.

### `04_retrieval_tests.ipynb`
Analyzes retrieval performance.

### `05_evaluation_analysis.ipynb`
Reviews evaluation results and quality trends.

---

## `experiments/`

Stores experimental configurations and results.

### `prompt_versions/`
Different prompt template versions tested during development.

### `retrieval_configs/`
Different retrieval pipeline configurations.

- `baseline.yaml` — initial retrieval setup
- `hybrid.yaml` — hybrid retrieval setup
- `rerank.yaml` — reranking-enhanced setup

### `results/`
Stores experiment outputs.

- `retrieval/` — retrieval experiment results
- `generation/` — answer generation experiment results
- `latency/` — latency and performance measurements

---

## `deployment/`

Contains deployment and infrastructure-related files.

### `backend.Dockerfile`
Docker image definition for the backend.

### `frontend.Dockerfile`
Docker image definition for the frontend.

### `nginx.conf`
Nginx configuration for serving frontend or reverse proxying backend requests.

### `render.yaml`
Deployment configuration for Render.

### `railway.json`
Deployment configuration for Railway.

### `github_actions/ci.yml`
Continuous integration workflow for testing and validation.

---

## Summary

The project is divided into several major parts:

- `backend/` — API, RAG pipeline, services, database, evaluation
- `frontend/` — user interface
- `data/` — raw, processed, embeddings, and evaluation data
- `docs/` — project documentation
- `experiments/` — prompt and retrieval experiments
- `notebooks/` — development research notebooks
- `deployment/` — Docker and hosting configuration

This structure is designed to keep the system modular, readable, and easy to extend as the project grows.