# DEVELOPER GUIDE
## Legal Contract Red-Flag Scanner

---

# Purpose

This document explains how to set up, run, maintain, and contribute to the project.

It serves as the onboarding guide for any developer (including future you) who works on this project.

Unlike the AI Handoff document, this guide focuses on practical development tasks.

---

# Project Structure

```
RED-FLAG/

│

├── backend/

│   ├── app/

│   ├── requirements.txt

│   ├── .env

│   └── .venv/

│

├── frontend/

│

├── docs/

│

├── sample_contracts/

│

└── README.md
```

---

# Technology Stack

| Component | Technology |
|-----------|------------|
| Language | Python |
| Backend | FastAPI |
| Frontend | Streamlit |
| AI Framework | LangChain |
| Local LLM | Ollama |
| Cloud LLM | Gemini |
| Validation | Pydantic |
| Configuration | Pydantic Settings |
| Database | SQLite (Planned) |
| ORM | SQLAlchemy (Planned) |
| Version Control | Git |

---

# Development Environment

Operating System

Windows 11

Editor

Visual Studio Code

Terminal

VS Code Integrated Terminal

Python Version

Python 3.12+

---

# First-Time Project Setup

## Clone Repository

```bash
git clone https://github.com/AdarshSharma2510/RED-FLAG.git
```

---

## Enter Project

```bash
cd RED-FLAG
```

---

## Create Virtual Environment

```bash
cd backend

python -m venv .venv
```

---

## Activate Virtual Environment

Windows

```powershell
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Create Environment File

Create

```
backend/.env
```

Example

```text
APP_NAME=Legal Contract Red-Flag Scanner

APP_VERSION=1.0.0

MODEL_PROVIDER=ollama

MODEL_NAME=llama3.1

DATABASE_URL=sqlite:///scanner.db

GEMINI_API_KEY=
```

---

# Running the Backend

Move into

```
backend
```

Run

```bash
uvicorn app.main:app --reload
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

OpenAPI JSON

```
http://127.0.0.1:8000/openapi.json
```

---

# Running Streamlit

Move into

```
frontend
```

Run

```bash
streamlit run app.py
```

---

# Git Workflow

Check status

```bash
git status
```

Add changes

```bash
git add .
```

Commit

```bash
git commit -m "Meaningful commit message"
```

Push

```bash
git push
```

---

# Commit Message Style

Good

```
Implement clause-aware document splitter

Add document processor

Implement rule matching engine

Integrate Gemini analyzer
```

Bad

```
Updated code

Fixed stuff

Changes

Final

Test
```

---

# Branch Strategy

Current strategy

Single branch

```
main
```

Future

```
main

feature/document-processing

feature/rule-engine

feature/frontend
```

---

# Coding Standards

Always

✅ Use type hints

✅ Keep functions small

✅ Use meaningful variable names

✅ Follow Single Responsibility Principle

✅ Separate business logic from API

✅ Write reusable modules

Avoid

❌ Giant files

❌ Duplicate code

❌ Hardcoded values

❌ Business logic inside routes

❌ Mixing AI logic with rule logic

---

# Folder Responsibilities

api/

HTTP routes only.

services/

Business logic.

rules/

Deterministic legal rules.

ai/

LLM communication.

schemas/

Pydantic models.

database/

Persistence layer.

utils/

Shared helper functions.

---

# Adding a New API Endpoint

1.

Create route

```
app/api/routes/
```

↓

2.

Add endpoint

↓

3.

Import router

↓

4.

Register in

```
api/router.py
```

---

# Adding a New Rule

Edit

```
rules/legal_rules.py
```

Add

- keyword
- severity
- explanation

The Rule Engine will automatically evaluate it.

---

# Adding a New LLM

Current

- Ollama

- Gemini

Future

- Claude

- OpenAI

- DeepSeek

Only modify

```
app/ai/
```

Business logic should remain unchanged.

---

# Running Tests

(Currently Planned)

Future command

```bash
pytest
```

---

# Updating Documentation

Whenever a milestone is completed update

```
00_MASTER_CONTEXT.md

02_ROADMAP.md

03_DECISIONS.md

04_INTERVIEW_NOTES.md

05_CHANGELOG.md
```

if necessary.

Documentation is considered part of the implementation.

---

# Common Git Commands

Current branch

```bash
git branch
```

View log

```bash
git log --oneline
```

View remotes

```bash
git remote -v
```

Fetch

```bash
git fetch
```

Pull

```bash
git pull
```

Push

```bash
git push
```

---

# Common Problems

## FastAPI Import Error

Usually caused by

- incorrect import
- missing __init__.py
- wrong module path

---

## Environment Variables Not Loading

Check

- .env location
- variable names
- Pydantic Settings

---

## Git Push Rejected

Usually caused by

- remote ahead
- authentication
- wrong account
- merge conflict

---

## Module Not Found

Check

- virtual environment activated
- dependencies installed
- correct working directory

---

# Debugging Checklist

Before asking for help

□ Virtual environment activated

□ Dependencies installed

□ Correct working directory

□ Backend running

□ .env loaded

□ Imports correct

□ Git status clean

---

# Development Workflow

Every feature follows the same workflow.

```
Understand the Problem

↓

Discuss Architecture

↓

Implement

↓

Test

↓

Git Commit

↓

Push

↓

Update Documentation

↓

Interview Questions
```

---

# Definition of Done

A feature is complete only when

✅ Code works

✅ Code explained

✅ Tested

✅ Committed

✅ Pushed

✅ Documentation updated

✅ Interview questions prepared

---

# Important Project Principles

- Build for understanding, not speed.
- Prefer maintainability over clever code.
- Keep modules independent.
- Explain design decisions.
- Follow incremental development.
- Treat documentation as part of the project.
- Every major architectural decision should be recorded.

---

# Last Updated

Version: 0.3.0