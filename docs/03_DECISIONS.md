# Architecture Decisions

## Decision #001

### Title
Use Streamlit instead of React

### Status
✅ Accepted

### Reason
The user already knows Python. Streamlit enables rapid development without learning a new frontend framework.

---

## Decision #002

### Title
Use LangChain Document Loaders

### Status
✅ Accepted

### Reason
Provides standardized loading for TXT, PDF, and DOCX while preserving metadata.

---

## Decision #003

### Title
Do not use RecursiveCharacterTextSplitter

### Status
✅ Accepted

### Reason
Character-based chunking can break legal clauses. The project will implement clause-aware splitting.

---

## Decision #004

### Title
Postpone Database Integration

### Status
✅ Accepted

### Reason
A working AI pipeline is a higher priority than persistence. The architecture already supports adding a database later.

---

## Decision #005

### Title
Use Modular Document Services

### Status
✅ Accepted

### Reason
Separate `loader.py`, `cleaner.py`, `splitter.py`, and `processor.py` to maintain the Single Responsibility Principle (SRP).