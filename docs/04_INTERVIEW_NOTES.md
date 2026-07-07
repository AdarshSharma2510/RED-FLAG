# INTERVIEW PREPARATION NOTES
## Legal Contract Red-Flag Scanner

---

# Purpose

This document contains interview questions and answers related to the Legal Contract Red-Flag Scanner project.

The goal is not to memorize answers but to understand the reasoning behind every architectural and implementation decision.

Questions are added after every completed milestone.

---

# Section 1 — Project Overview

---

## Question

Tell me about your project.

### Good Answer

The project is an AI-powered Legal Contract Red-Flag Scanner that analyzes contracts such as Terms of Service, rental agreements, and software licenses. It detects potentially risky clauses using a hybrid approach that combines a deterministic rule engine with Large Language Models. The backend is built with FastAPI, document processing is handled using LangChain, AI responses are structured with Pydantic, and the interface is built using Streamlit.

---

### Follow-up Questions

- Why did you build it?
- What problem does it solve?
- Who are the target users?

---

### Avoid Saying

- "It just uses AI."
- "The LLM finds everything."
- "It is just a college project."

---

# Section 2 — Technology Stack

---

## Question

Why did you choose FastAPI?

### Good Answer

FastAPI provides excellent performance, asynchronous request handling, automatic API documentation through OpenAPI, and integrates naturally with Pydantic for request and response validation.

---

### Follow-up Questions

- Why not Flask?
- Why not Django?

---

### Avoid Saying

- "FastAPI is faster."
- "Everyone uses FastAPI."

Explain the actual advantages.

---

## Question

Why Pydantic?

### Good Answer

Pydantic provides runtime validation, automatic serialization, strong typing, and acts as the contract between different layers of the application. It reduces bugs and improves maintainability.

---

### Follow-up Questions

- Why not dictionaries?
- Difference between dataclasses and Pydantic?

---

### Avoid Saying

- "Because FastAPI needs it."

---

## Question

Why LangChain?

### Good Answer

LangChain is used only where it adds value. It standardizes document loading across multiple formats and simplifies communication with different LLM providers. Business logic remains independent from LangChain.

---

### Follow-up Questions

- Why not use Gemini directly?
- What parts of LangChain are you using?

---

### Avoid Saying

- "LangChain runs the whole application."

---

## Question

Why Streamlit?

### Good Answer

The objective of this project is to demonstrate backend engineering and AI integration rather than frontend development. Streamlit allows rapid development of a clean interface while keeping the focus on the core AI pipeline.

---

### Follow-up Questions

- Why not React?
- What are Streamlit's limitations?

---

### Avoid Saying

- "I didn't want to learn React."

Instead, emphasize project priorities.

---

# Section 3 — Software Architecture

---

## Question

Why did you separate the project into multiple services?

### Good Answer

The project follows the Single Responsibility Principle. Each service performs one task only, making the code easier to test, maintain, and replace independently.

---

### Follow-up Questions

- Give an example.
- What happens if you merge everything into one file?

---

### Avoid Saying

- "It looks cleaner."

Mention maintainability and modularity.

---

## Question

Why keep the Rule Engine separate from the AI?

### Good Answer

Rules provide deterministic behavior for known patterns, while the LLM performs semantic reasoning. Separating them reduces cost, improves explainability, and avoids unnecessary LLM calls.

---

### Follow-up Questions

- Why not let the LLM analyze everything?
- What are the advantages of a hybrid system?

---

### Avoid Saying

- "AI is too expensive."

Mention performance, determinism, and explainability.

---

## Question

Why delay database implementation?

### Good Answer

The primary objective is to build a working document analysis pipeline. Because the architecture is modular, persistence can be added later without changing the processing logic.

---

### Follow-up Questions

- Would this decision change in production?
- How would you integrate SQLAlchemy later?

---

### Avoid Saying

- "The database wasn't important."

---

# Section 4 — Git & Development

---

## Question

How did you manage version control?

### Good Answer

I used Git throughout the project, creating logical commits after each completed feature. The repository was hosted on GitHub, and I documented architectural decisions alongside the code.

---

### Follow-up Questions

- Describe a Git issue you solved.
- What is a merge conflict?

---

### Avoid Saying

- "I only know git add and git push."

---

# Section 5 — AI Design

---

## Question

Why not send the whole document directly to the LLM?

### Good Answer

Large contracts can exceed context limits and increase cost. The application first splits the document into legal clauses, filters suspicious ones using the Rule Engine, and only then sends relevant content to the LLM.

---

### Follow-up Questions

- Why clause-aware splitting?
- Why not RecursiveCharacterTextSplitter?

---

### Avoid Saying

- "Because the context window is small."

Explain efficiency and accuracy.

---

# Section 6 — Future Questions

This section will grow throughout development.

Topics to be added:

- LangChain Chains
- Prompt Engineering
- Structured Output
- Ollama
- Gemini
- SQLAlchemy
- SQLite
- Streamlit
- Rule Engine
- Testing
- Logging
- Performance
- Production Readiness

---

# Personal Interview Tips

- Explain the reasoning before the implementation.
- Mention trade-offs.
- Use examples from this project.
- Be honest if you don't know something.
- Avoid memorized answers.
- Focus on architecture, maintainability, and design decisions.

---

# Last Updated

Version: 0.3.0

This document is updated after every major milestone.