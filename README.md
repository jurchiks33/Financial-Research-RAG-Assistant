# Financial Research RAG Assistant

A work-in-progress AI application that answers finance-related questions from uploaded documents using Retrieval-Augmented Generation (RAG).

The goal of this project is to build a modern end-to-end AI system that can ingest financial documents, process and index them, retrieve relevant evidence, and generate grounded answers with citations through a clean user interface.

---

## Project Status

This project is currently in the **initial setup and architecture phase**.

Current focus:
- defining project structure
- documenting architecture
- preparing backend and frontend foundations
- planning ingestion, retrieval, generation, and evaluation pipeline

This repository will grow step by step into a full-stack AI application.

---

## Project Goal

The main goal is to build a **Financial Research RAG Assistant** that can help users explore and question financial documents such as:

- annual reports
- earnings call transcripts
- macroeconomic reports
- research notes

The assistant should return answers based on retrieved source material rather than unsupported model output.

---

## Planned Features

### Document Ingestion
- upload and manage financial documents
- parse text from PDF, DOCX, TXT, and similar formats
- extract useful metadata such as title, company, year, and document type

### Preprocessing
- clean extracted text
- split documents into retrieval-friendly chunks
- store chunk metadata for filtering and traceability

### Embeddings and Retrieval
- generate embeddings for document chunks
- store vectors in a vector database
- retrieve relevant chunks based on user questions
- support retrieval inspection and debugging

### Answer Generation
- generate answers grounded in retrieved content
- include source citations
- reduce hallucinations with guardrails and evidence checks

### Evaluation
- measure retrieval relevance
- measure answer quality
- maintain benchmark datasets for testing and improvement

### User Interface
- document upload page
- chat page for asking questions
- evaluation dashboard
- admin/debugging views

---

## Tech Stack

### Backend
- Python
- FastAPI

### Frontend
- React
- TypeScript
- Vite

### AI / Retrieval
- embeddings API or embedding model
- vector database such as Qdrant or pgvector
- LLM for answer generation
- reranking and evaluation components

### Development / Deployment
- Docker
- GitHub
- Markdown documentation

---

## Project Structure

The project is organized into backend, frontend, data, experiments, documentation, and deployment layers.

Main documentation files:
- `docs/project_structure.md`
- `docs/project_structure_explained.md`
- `docs/architecture.md`
- `docs/setup_guide.md`

---

## Current Repository Focus

At this stage, the repository is focused on:

- planning the full project structure
- documenting components clearly
- setting up a professional foundation for development
- making the project easy to understand for recruiters, collaborators, and future maintainers

---

## Development Roadmap

### Phase 1 — Foundation
- [x] define project idea
- [x] define folder structure
- [x] create initial documentation
- [x] create initial `.gitignore`
- [x] create environment configuration template
- [x] set up backend foundation
- [x] set up frontend foundation

### Phase 2 — Core RAG Pipeline
- [x] document upload flow
- [x] parsing and preprocessing
- [x] chunking logic
- [x] embeddings generation
- [x] vector storage
- [x] retrieval pipeline
- [x] answer generation with citations

Phase 2 completed:
- End-to-end RAG pipeline is operational
- Chat query endpoint returns grounded answers with inline citations
- Retrieval results are linked back to source chunks

### Phase 3 — Evaluation and Quality
- [ ] retrieval benchmark dataset
- [ ] answer evaluation workflow
- [ ] feedback collection
- [ ] quality metrics dashboard

### Phase 4 — Frontend Experience
- [ ] chat interface
- [ ] document management page
- [ ] evaluation dashboard
- [ ] admin tools

### Phase 5 — Deployment
- [ ] Docker setup
- [ ] local multi-service run
- [ ] deployment configuration
- [ ] CI pipeline

---

## Design Principles

This project is being built with the following principles in mind:

- modular structure
- clear separation of concerns
- source-grounded answers
- evaluation-first mindset
- maintainable full-stack design
- professional documentation from the start

---

## Why This Project

This project is intended to demonstrate practical skills in:

- AI application development
- Retrieval-Augmented Generation
- document ingestion pipelines
- backend API design
- frontend application structure
- evaluation and quality measurement
- production-style project organization


---

## Notes

This is an active work in progress.  
Some folders and files are currently placeholders and will be implemented gradually as development continues.

---

## License

License to be added later.