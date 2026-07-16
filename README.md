# 🚩 RED FLAG — AI-Powered Legal Contract Risk Analyzer

RED FLAG is an AI-powered Legal Contract Risk Analyzer that helps users identify potentially risky clauses in legal documents. Users can upload a contract in PDF, DOCX, or TXT format, and the application automatically detects predefined legal risks before generating AI-powered explanations, legal consequences, and recommendations. The project demonstrates the integration of traditional rule-based systems with Large Language Models (LLMs) to provide meaningful contract analysis through a clean and modern user interface.

> **Disclaimer:** RED FLAG is intended for educational and portfolio purposes only and does not provide legal advice.

---

## ✨ Features

- 📄 Upload contracts in **PDF**, **DOCX**, and **TXT** formats
- 🤖 AI-generated legal risk summaries using **Google Gemini**
- ⚖️ Rule-based detection of common legal contract risks
- 📊 Risk severity classification (**HIGH**, **MEDIUM**, **LOW**)
- 💡 AI-generated recommendations and legal consequences
- 🎨 Modern, responsive React interface
- 📋 Professional report-style results screen
- 🔄 Drag & drop file upload
- 📱 Responsive design for desktop and mobile

---

## 🏗️ Architecture

```text
                    +----------------------+
                    |   React Frontend     |
                    |----------------------|
                    | Upload Contract UI   |
                    | Loading Screen       |
                    | Results Dashboard    |
                    +----------+-----------+
                               |
                               | HTTP (Axios)
                               |
                    +----------v-----------+
                    |     FastAPI API      |
                    +----------+-----------+
                               |
             +-----------------+------------------+
             |                                    |
             |                                    |
    Rule-Based Risk Engine                 Google Gemini
      (Legal Rules)                    (AI Analysis via LangChain)
             |                                    |
             +-----------------+------------------+
                               |
                       JSON Response
                               |
                        React Frontend
```

---

## 🛠️ Tech Stack

### Frontend

- React
- Vite
- Tailwind CSS
- Axios
- Lucide React

### Backend

- FastAPI
- LangChain
- Google Gemini
- Rule-Based Legal Risk Detection

---

## 📂 Project Structure

```text
RED FLAG
│
├── backend/
│   ├── app/
│   ├── data/
│   ├── models/
│   ├── services/
│   └── main.py
│
└── frontend/
    ├── src/
    │   ├── components/
    │   ├── services/
    │   ├── assets/
    │   ├── App.jsx
    │   └── main.jsx
    │
    ├── package.json
    └── vite.config.js
```

---

## ⚙️ How It Works

1. Upload a legal contract.
2. The frontend sends the file to the FastAPI backend.
3. The backend extracts and cleans the document text.
4. A rule engine scans the document for predefined legal risks.
5. Detected clauses are analyzed using Google Gemini.
6. The frontend presents a structured report including:
   - Severity
   - Category
   - Explanation
   - Matched Text
   - Clause Text
   - Risk Summary
   - Legal Consequence
   - Recommendation
   - Confidence Score

---

## 📊 Example Workflow

```text
Upload Contract
       │
       ▼
Text Extraction
       │
       ▼
Rule-Based Detection
       │
       ▼
Google Gemini Analysis
       │
       ▼
Structured Risk Report
```

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/yourusername/RED-FLAG.git
cd RED-FLAG
```

---

### Backend Setup

```bash
cd backend

python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend runs on:

```
http://127.0.0.1:8000
```

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

---

### Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on:

```
http://localhost:5173
```

---

## 📌 Supported File Types

- PDF
- DOCX
- TXT

---

## 📄 Sample Output

Each detected risk includes:

- Severity
- Category
- Clause ID
- Sentence ID
- Trigger Source
- Explanation
- Matched Text
- Clause Text
- Risk Summary
- Legal Consequence
- Recommendation
- Confidence Score

---

## 🎯 Project Goals

This project was developed to demonstrate:

- AI integration in real-world software
- Rule-based NLP systems
- Large Language Model integration
- REST API development with FastAPI
- Modern React frontend development
- Clean software architecture
- Professional UI/UX design
- Resume-quality full-stack engineering

---

## 🔮 Future Improvements

- Additional legal rule sets
- Clause highlighting within uploaded documents
- PDF export for analysis reports
- Improved AI explanations
- Dark mode
- Deployment with Docker
- Enhanced accessibility

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Adarsh Sharma**

Computer Science Engineering Student

Built as a portfolio project to demonstrate AI-powered software engineering, modern frontend development, and backend integration using FastAPI, LangChain, and Google Gemini.