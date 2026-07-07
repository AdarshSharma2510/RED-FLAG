# SYSTEM ARCHITECTURE
## Legal Contract Red-Flag Scanner

---

# Purpose

This document describes the architecture of the Legal Contract Red-Flag Scanner.

It explains how every major component interacts with the others, why the project is organized in this way, and the engineering principles followed throughout development.

This document focuses on system design rather than implementation details.

---

# High-Level Architecture

```
                User
                  │
                  ▼
         Streamlit Frontend
                  │
                  ▼
          FastAPI Backend API
                  │
                  ▼
            Scan Service
                  │
     ┌────────────┴────────────┐
     ▼                         ▼
Document Processing       Rule Engine
     │                         │
     ▼                         ▼
ExtractedDocument         Rule Findings
     │                         │
     └────────────┬────────────┘
                  ▼
             AI Analyzer
                  │
                  ▼
          Structured Findings
                  │
                  ▼
           Streamlit Results
```

---

# Layered Architecture

The project follows a layered architecture.

```
Presentation Layer
        │
        ▼
API Layer
        │
        ▼
Service Layer
        │
        ▼
Rule Engine
        │
        ▼
AI Layer
        │
        ▼
Data Layer (Future)
```

Each layer only communicates with the layer directly below it.

This minimizes coupling between components.

---

# Backend Architecture

```
FastAPI

│

├── API Layer

│       Handles HTTP requests

│

├── Services

│       Business Logic

│

├── Rules

│       Rule Evaluation

│

├── AI

│       LLM Communication

│

├── Schemas

│       Data Models

│

└── Database

        Persistence (Future)
```

---

# Request Flow

When a user uploads a document:

```
User Upload

↓

FastAPI Endpoint

↓

Scan Service

↓

Document Loader

↓

Text Cleaner

↓

Clause Splitter

↓

Sentence Splitter

↓

ExtractedDocument

↓

Rule Engine

↓

Potential Findings

↓

LLM Verification

↓

AnalysisResult

↓

FastAPI Response

↓

Streamlit UI
```

---

# Document Processing Pipeline

The document processing subsystem is responsible for converting uploaded files into structured legal clauses.

```
TXT / PDF / DOCX

↓

LangChain Document Loader

↓

Raw Text

↓

Text Cleaner

↓

Cleaned Text

↓

Clause Splitter

↓

Sentence Splitter

↓

ExtractedDocument
```

The output of this pipeline is completely independent from AI.

---

# Rule Engine Pipeline

```
ExtractedDocument

↓

Clause

↓

Sentence

↓

Rule Evaluation

↓

Matched Rules

↓

Finding Objects

↓

LLM Validation

↓

AnalysisResult
```

The Rule Engine is responsible for reducing the amount of work performed by the LLM.

Only suspicious clauses should be sent to the language model.

---

# AI Pipeline

```
Finding

↓

Prompt Builder

↓

Gemini / Ollama

↓

Structured Output

↓

Pydantic Validation

↓

AnalysisResult
```

The AI layer is responsible only for semantic reasoning.

Business rules should never exist inside prompts.

---

# Folder Responsibilities

## api/

Responsible for HTTP endpoints.

Contains:

- Routers
- Request handling
- Response generation

Never contains business logic.

---

## services/

Responsible for application logic.

Contains:

- Document processing
- Scan orchestration

Never contains HTTP handling.

---

## services/document/

Responsible for document processing.

Modules:

loader.py

Loads TXT, PDF and DOCX files.

cleaner.py

Normalizes extracted text.

splitter.py

Splits cleaned text into clauses and sentences.

processor.py

Coordinates the entire document pipeline.

---

## rules/

Responsible for deterministic legal analysis.

Contains:

- Rule definitions
- Rule engine

Never communicates directly with the frontend.

---

## ai/

Responsible for communication with language models.

Contains:

- Prompt templates
- LangChain chains
- Gemini
- Ollama

Never contains business logic.

---

## schemas/

Responsible for all shared data models.

Contains:

- Request models
- Response models
- Internal processing models

Every layer communicates using schemas.

---

## database/

Responsible for persistence.

(Currently deferred.)

Will eventually contain:

- SQLAlchemy models
- CRUD operations
- Session management

---

# Engineering Principles

The architecture follows these principles.

## Single Responsibility Principle

Each module performs exactly one task.

Examples:

Document Loader

Loads files.

Text Cleaner

Cleans text.

Clause Splitter

Splits clauses.

Rule Engine

Evaluates rules.

AI Analyzer

Performs semantic reasoning.

---

## Separation of Concerns

Each subsystem is isolated.

Document processing never performs AI.

AI never loads files.

Rules never communicate with HTTP.

FastAPI never performs business logic.

---

## Modularity

Every component should be replaceable.

Example:

Today:

Gemini

Tomorrow:

Claude

Only the AI module changes.

The rest of the application remains untouched.

---

## Extensibility

Future improvements should require minimal modifications.

Examples:

- New document formats
- Additional rules
- Different LLM providers
- Database support
- Authentication

---

# Dependency Direction

The project follows one-way dependencies.

```
Frontend

↓

API

↓

Services

↓

Rules

↓

AI

↓

Database
```

Upper layers never depend on implementation details of lower layers.

---

# Future Architecture

Later versions will introduce:

```
SQLite

↓

SQLAlchemy

↓

Scan History

↓

Analytics Dashboard

↓

User Preferences
```

These additions should require minimal changes because the current architecture is designed to support them.

---

# Architecture Summary

The project is designed around:

- Clean Architecture principles
- Modular services
- Layered design
- Separation of concerns
- Hybrid rule-based and AI analysis
- Independent document processing
- Production-grade maintainability

This architecture prioritizes maintainability, explainability, extensibility, and readability over writing the smallest amount of code.