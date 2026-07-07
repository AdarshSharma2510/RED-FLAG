# PROJECT ROADMAP
## Legal Contract Red-Flag Scanner

---

# Project Status

**Current Version:** v0.3.0

**Overall Progress**

██████████░░░░░░░░░░░░░░░░░░░░░░ 30%

Current Milestone:

🟡 Document Processing Pipeline

---

# Phase 1 — Project Foundation

## Goal

Create the project structure and backend foundation.

### Tasks

- [x] Create project directory
- [x] Setup FastAPI
- [x] Configure virtual environment
- [x] Setup Git repository
- [x] Connect GitHub repository
- [x] Create folder architecture
- [x] Configure environment variables
- [x] Configure Pydantic Settings
- [x] Create documentation system

**Status:** ✅ Complete

---

# Phase 2 — Core Data Models

## Goal

Create reusable schemas used across the project.

### Tasks

- [x] Sentence schema
- [x] Clause schema
- [x] ExtractedDocument schema
- [x] Finding schema
- [x] Analysis schema
- [x] Rule schema

**Status:** ✅ Complete

---

# Phase 3 — Document Processing

## Goal

Convert uploaded contracts into structured legal clauses.

### Tasks

- [x] LangChain document loader
- [x] Text cleaner
- [ ] Clause splitter
- [ ] Sentence splitter
- [ ] Document processor
- [ ] Unit testing

**Status:** 🟡 In Progress

---

# Phase 4 — Rule Engine

## Goal

Identify potentially risky clauses without using AI.

### Tasks

- [x] Rule structure
- [x] Rule definitions
- [ ] Rule matching
- [ ] Finding generation
- [ ] Severity classification
- [ ] Rule testing

**Status:** 🟡 In Progress

---

# Phase 5 — AI Analysis

## Goal

Use LLMs to explain why clauses are risky.

### Tasks

- [ ] Prompt engineering
- [ ] LangChain integration
- [ ] Ollama integration
- [ ] Gemini integration
- [ ] Structured Pydantic output
- [ ] AI validation

**Status:** 🔴 Not Started

---

# Phase 6 — Streamlit Frontend

## Goal

Create a clean interface for uploading and reviewing contracts.

### Tasks

- [ ] Upload page
- [ ] Results page
- [ ] Highlight risky clauses
- [ ] Severity colors
- [ ] Explanation panel
- [ ] Summary statistics

**Status:** 🔴 Not Started

---

# Phase 7 — Database

## Goal

Persist scan history for future improvements.

### Tasks

- [ ] SQLite setup
- [ ] SQLAlchemy models
- [ ] Scan history
- [ ] Finding history
- [ ] CRUD operations

**Status:** ⚪ Deferred

---

# Phase 8 — Testing & Quality

## Goal

Improve reliability and maintainability.

### Tasks

- [ ] Unit tests
- [ ] Integration tests
- [ ] Error handling
- [ ] Logging
- [ ] Performance improvements

**Status:** 🔴 Not Started

---

# Phase 9 — Resume Polish

## Goal

Prepare the project for interviews and GitHub.

### Tasks

- [ ] Complete README
- [ ] Architecture diagrams
- [ ] Sample contracts
- [ ] Demo screenshots
- [ ] Interview notes
- [ ] Final documentation

**Status:** 🔴 Not Started

---

# Stretch Goals (Optional)

These features are **not required** for the resume project but may be added later.

- [ ] OCR support
- [ ] Multi-language contracts
- [ ] Clause similarity search
- [ ] Vector database
- [ ] RAG for legal references
- [ ] Export analysis to PDF
- [ ] Scan comparison
- [ ] Analytics dashboard

---

# Current Focus

Current Phase:

**Phase 3 — Document Processing**

Current Task:

Implement

- `services/document/splitter.py`
- `services/document/processor.py`

After that:

- Connect the Rule Engine
- Generate structured Findings

---

# Definition of Done (Version 1.0)

The project will be considered complete when it can:

- Upload TXT, PDF and DOCX contracts
- Extract and clean document text
- Split contracts into clauses and sentences
- Detect risky clauses using rules
- Validate findings using an LLM
- Explain every detected issue
- Display highlighted clauses in Streamlit
- Run completely on a local machine
- Demonstrate clean architecture
- Be suitable as a portfolio project