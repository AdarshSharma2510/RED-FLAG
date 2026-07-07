# PROJECT MASTER CONTEXT
## Legal Contract Red-Flag Scanner

---

# Project Information

| Item | Value |
|------|------|
| Project Name | Legal Contract Red-Flag Scanner |
| Current Version | v0.3.0 |
| Current Phase | Document Processing Pipeline |
| Status | In Development |
| Repository | RED-FLAG |
| Last Updated | 2026-07-05 |

---

# Project Goal

The goal of this project is to build a production-grade AI-powered legal contract analyzer suitable for a software engineering / AI resume.

The application allows a user to upload legal contracts (TXT, PDF or DOCX), automatically extracts the text, detects potentially dangerous legal clauses, categorizes them according to severity, explains why they are risky and highlights them inside the original document.

This project is intentionally being developed as if it were a real software product rather than a tutorial project.

---

# Resume Objective

This project demonstrates practical knowledge of:

- Backend Development
- FastAPI
- REST APIs
- LangChain
- Local LLMs (Ollama)
- Cloud LLMs (Gemini)
- Prompt Engineering
- Hybrid AI Systems
- Rule Based NLP
- Document Processing
- Streamlit
- Software Architecture
- Git Workflow
- Clean Code Principles

---

# Project Scope

### Included

- Upload contracts
- PDF support
- DOCX support
- TXT support
- Document processing
- Rule based analysis
- LLM based semantic analysis
- Highlight risky clauses
- Severity classification
- Explanation generation
- Streamlit interface

### Not Included

- Live deployment
- Authentication
- User accounts
- Cloud database
- Team collaboration

These features are intentionally excluded because the goal is a high-quality resume project rather than a production SaaS application.

---

# Technology Stack

| Layer | Technology |
|--------|------------|
| Language | Python |
| Backend | FastAPI |
| Validation | Pydantic |
| Configuration | Pydantic Settings |
| AI Framework | LangChain |
| Local LLM | Ollama (Llama 3.1) |
| Cloud LLM | Google Gemini |
| Frontend | Streamlit |
| ORM | SQLAlchemy (Planned) |
| Database | SQLite (Planned) |
| Version Control | Git |
| Repository | GitHub |

---

# High Level Architecture

User Upload

↓

LangChain Document Loader

↓

Document Cleaner

↓

Clause Splitter

↓

Sentence Splitter

↓

Rule Engine

↓

LLM Analyzer

↓

Structured Findings

↓

Streamlit Frontend

---

# Development Philosophy

This project follows several engineering principles.

## 1. Single Responsibility Principle

Every module has exactly one responsibility.

Examples

loader.py

Only loads documents.

cleaner.py

Only cleans text.

splitter.py

Only splits text.

processor.py

Only orchestrates the document pipeline.

rule_engine.py

Only evaluates rules.

---

## 2. Business Logic Independence

Business logic should never depend directly on LangChain.

LangChain is only an implementation detail.

If LangChain is removed tomorrow, only loader.py and the AI orchestration should require changes.

---

## 3. Incremental Development

Features are built in small, testable steps.

Every stage should leave the application in a working state.

---

## 4. Explainability First

The project should always be able to explain WHY something was flagged.

The LLM should never simply output:

"This looks risky."

It should explain:

- what clause was found
- why it is risky
- what rule triggered
- severity

---

## 5. Production Style Architecture

The project prioritizes clean architecture over writing the shortest amount of code.

---

# Current Folder Structure

backend/

app/

ai/

api/

core/

database/

models/

rules/

legal_rules.py

rule_engine.py

schemas/

analysis.py

document.py

finding.py

rule.py

services/

document/

loader.py

cleaner.py

scan/

utils/

main.py

frontend/

docs/

sample_contracts/

---

# Schema Overview

## Sentence

Represents the smallest unit of analysis.

Fields

- id
- text

---

## Clause

Represents one logical legal clause.

Fields

- id
- text
- sentences

Future fields

- title
- section

---

## ExtractedDocument

Represents the processed document after extraction.

Fields

- filename
- raw_text
- cleaned_text
- clauses

---

# Current Pipeline

Document Upload

↓

Loader

↓

Raw Text

↓

Cleaner

↓

Cleaned Text

↓

Clause Splitter

↓

Sentence Splitter

↓

ExtractedDocument

↓

Rule Engine

↓

LLM

↓

AnalysisResult

---

# Completed Modules

✅ Project Planning

✅ Folder Structure

✅ FastAPI Setup

✅ Git & GitHub

✅ Environment Variables

✅ Configuration Management

✅ Pydantic Schemas

✅ LangChain Loader Design

✅ Text Cleaner Design

---

# Current Milestone

Document Processing Pipeline

The next objective is to build:

splitter.py

processor.py

These components will transform cleaned text into structured Clause and Sentence objects.

---

# Future Milestones

- Clause-aware parser
- Rule Engine
- Scan Service
- Gemini Integration
- Ollama Integration
- Streamlit Interface
- Database
- Testing
- Logging
- Documentation
- Resume Polish

---

# Important Engineering Decisions

The following decisions have already been made.

- Streamlit instead of React.
- LangChain only for document loading and AI orchestration.
- Rule Engine before the LLM.
- Clause-aware parsing instead of character chunking.
- Database postponed until pipeline completion.
- Modular services following SRP.

See:

03_DECISIONS.md

---

# Development Workflow

Every feature follows the same workflow.

1. Explain the concept.
2. Discuss architecture.
3. Design the implementation.
4. Write the code.
5. Test the feature.
6. Commit to Git.
7. Push to GitHub.
8. Update documentation.
9. Discuss interview questions.

---

# Teaching Methodology

This project is intentionally educational.

The assistant should always:

- Explain concepts before implementation.
- Explain why a design choice was made.
- Explain every major technology introduced.
- Build incrementally.
- Avoid skipping architectural reasoning.
- Include interview preparation after major milestones.

The goal is not only to finish the project but to ensure the developer understands every component deeply.

---

# Current Status

Overall Progress

██████████░░░░░░░░░░░░░░░░░░░░░░ 30%

Current Focus

Document Processing

Current Task

Implement

services/document/splitter.py

services/document/processor.py

---

# End of Master Context

This document is the primary source of truth for the project.

Whenever a new AI session begins, this document should be provided first before continuing development.