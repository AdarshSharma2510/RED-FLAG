# CHANGELOG
## Legal Contract Red-Flag Scanner

All notable changes to this project will be documented in this file.

The format loosely follows the "Keep a Changelog" convention.

---

# [0.3.0] - 2026-07-05

## Added

### Project Foundation

- Created project directory structure
- Initialized Git repository
- Connected GitHub repository
- Configured Python virtual environment

### Backend

- Created FastAPI application
- Added API router structure
- Configured environment variables
- Added configuration management using Pydantic Settings

### Schemas

Added initial project schemas:

- Sentence
- Clause
- ExtractedDocument
- Finding
- Analysis
- Rule

### Document Processing

Added document processing foundation.

Implemented:

- LangChain document loading
- Text cleaning service

Designed:

- Clause-aware splitting architecture
- Document processing pipeline

### Rules

Added:

- Rule definitions
- Rule Engine architecture

### Documentation

Created project documentation system.

Added:

- PROJECT_MASTER_CONTEXT
- ARCHITECTURE
- ROADMAP
- DECISIONS
- INTERVIEW_NOTES
- CHANGELOG

---

## Changed

- Switched frontend plan from React to Streamlit.
- Delayed database implementation until after the AI pipeline.
- Changed document processing strategy from character-based chunking to clause-aware splitting.

---

## Fixed

- FastAPI import issues
- API router configuration
- Environment variable loading
- GitHub authentication
- Git remote configuration
- Git merge issues
- Repository synchronization

---

## Deferred

The following features were intentionally postponed.

- SQLite integration
- SQLAlchemy models
- Scan history
- User management
- Authentication
- Production deployment

---

## Current Progress

Completed

- Project planning
- Backend setup
- Git workflow
- Configuration
- Schemas
- Loader
- Cleaner

Currently Working On

- Clause Splitter
- Document Processor

Next Milestone

Complete the Document Processing Pipeline.

---

# Upcoming Versions

## Version 0.4.0

Planned

- Clause Splitter
- Sentence Splitter
- Document Processor

---

## Version 0.5.0

Planned

- Rule Engine implementation
- Finding generation
- Severity scoring

---

## Version 0.6.0

Planned

- Gemini integration
- Ollama integration
- Prompt engineering
- Structured AI outputs

---

## Version 0.7.0

Planned

- Streamlit frontend
- Risk highlighting
- Results dashboard

---

## Version 0.8.0

Planned

- SQLite
- SQLAlchemy
- Scan history

---

## Version 1.0.0

Target Release

Features

- End-to-end legal contract scanner
- Hybrid Rule Engine + AI
- Streamlit interface
- Local LLM support
- Gemini support
- Documentation
- Resume ready