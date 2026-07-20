# # # # This file only exists so that in GitHub this project shows as a Python project and not a JavaScript project. 

# # # # So I am just randomly babbling stuff

# # # # Another line.

# # # # Another line.
# # # # Another line.




# # # # Another line.



# # # # Another line.



# # # # Another line.




# # # # Another line.



# # # print("Hello World")

# # # # Since this file will not be used anywhere. I can just do this and call it a day i guess. 

# # # # Lets see if it happened or not


# # # # 🚩 RED FLAG — AI-Powered Legal Contract Risk Analyzer

# # # RED FLAG is an AI-powered Legal Contract Risk Analyzer that helps users identify potentially risky clauses in legal documents. Users can upload a contract in PDF, DOCX, or TXT format, and the application automatically detects predefined legal risks before generating AI-powered explanations, legal consequences, and recommendations. The project demonstrates the integration of traditional rule-based systems with Large Language Models (LLMs) to provide meaningful contract analysis through a clean and modern user interface.

# # # > **Disclaimer:** RED FLAG is intended for educational and portfolio purposes only and does not provide legal advice.

# # # ---

# # # ## 🌐 Live Demo

# # # **Frontend:** https://red-flag-nu.vercel.app

# # # **Backend API (Swagger):** https://red-flag-d2eh.onrender.com/docs

# # # ---


# # # ## ✨ Features

# # # - 📄 Upload contracts in **PDF**, **DOCX**, and **TXT** formats
# # # - 🤖 AI-generated legal risk summaries using **Google Gemini**
# # # - ⚖️ Rule-based detection of common legal contract risks
# # # - 📊 Risk severity classification (**HIGH**, **MEDIUM**, **LOW**)
# # # - 💡 AI-generated recommendations and legal consequences
# # # - 🎨 Modern, responsive React interface
# # # - 📋 Professional report-style results screen
# # # - 🔄 Drag & drop file upload
# # # - 📱 Responsive design for desktop and mobile

# # # ---

# # # ## 🏗️ Architecture

# # # ```text
# # #                            +----------------------+
# # #                            |        User          |
# # #                            +----------+-----------+
# # #                                       |
# # #                                       |
# # #                                       v
# # #                     +-------------------------------+
# # #                     |  Vercel (React + Vite)        |
# # #                     |-------------------------------|
# # #                     | • Upload Contract UI          |
# # #                     | • Loading Screen              |
# # #                     | • Results Dashboard           |
# # #                     +---------------+---------------+
# # #                                     |
# # #                                     | HTTPS (Axios)
# # #                                     |
# # #                                     v
# # #                     +-------------------------------+
# # #                     | Render (FastAPI Backend)      |
# # #                     +---------------+---------------+
# # #                                     |
# # #                +--------------------+--------------------+
# # #                |                                         |
# # #                |                                         |
# # #       Rule-Based Risk Engine                 Google Gemini
# # #          (Legal Rules)                  (AI Analysis via LangChain)
# # #                |                                         |
# # #                +--------------------+--------------------+
# # #                                     |
# # #                              Structured JSON
# # #                                     |
# # #                                     |
# # #                                     v
# # #                          React Results Interface
# # # ```

# # # ---

# # # ## 🛠️ Tech Stack

# # # ### Frontend

# # # - React
# # # - Vite
# # # - Tailwind CSS
# # # - Axios
# # # - Lucide React

# # # ### Backend

# # # - FastAPI
# # # - LangChain
# # # - Google Gemini
# # # - Rule-Based Legal Risk Detection

# # # ### Deployment

# # # - Vercel (Frontend)
# # # - Render (Backend)

# # # ---

# # # ## 📂 Project Structure

# # # ```text
# # # RED FLAG
# # # │
# # # ├── backend/
# # # │   ├── app/
# # # │   ├── data/
# # # │   ├── models/
# # # │   ├── services/
# # # │   └── main.py
# # # │
# # # └── frontend/
# # #     ├── src/
# # #     │   ├── components/
# # #     │   ├── services/
# # #     │   ├── assets/
# # #     │   ├── App.jsx
# # #     │   └── main.jsx
# # #     │
# # #     ├── package.json
# # #     └── vite.config.js
# # # ```

# # # ---

# # # ## ⚙️ How It Works

# # # 1. Upload a legal contract.
# # # 2. The frontend sends the file to the FastAPI backend.
# # # 3. The backend extracts and cleans the document text.
# # # 4. A rule engine scans the document for predefined legal risks.
# # # 5. Detected clauses are analyzed using Google Gemini.
# # # 6. The frontend presents a structured report including:
# # #    - Severity
# # #    - Category
# # #    - Explanation
# # #    - Matched Text
# # #    - Clause Text
# # #    - Risk Summary
# # #    - Legal Consequence
# # #    - Recommendation
# # #    - Confidence Score

# # # ---

# # # ## 📊 Example Workflow

# # # ```text
# # # Upload Contract
# # #        │
# # #        ▼
# # # Text Extraction
# # #        │
# # #        ▼
# # # Rule-Based Detection
# # #        │
# # #        ▼
# # # Google Gemini Analysis
# # #        │
# # #        ▼
# # # Structured Risk Report
# # # ```

# # # ---

# # # ## 🚀 Getting Started

# # # ### Clone the repository

# # # ```bash
# # # git clone https://github.com/yourusername/RED-FLAG.git
# # # cd RED-FLAG
# # # ```

# # # ---

# # # ### Backend Setup

# # # ```bash
# # # cd backend

# # # python -m venv .venv

# # # # Windows
# # # .venv\Scripts\activate

# # # # Linux/macOS
# # # source .venv/bin/activate

# # # pip install -r requirements.txt

# # # uvicorn app.main:app --reload

# # # ---

# # # ### Frontend Setup

# # # ```bash
# # # cd frontend

# # # npm install

# # # npm run dev

# # # ---

# # # ## 📌 Supported File Types

# # # - PDF
# # # - DOCX
# # # - TXT

# # # ---

# # # ## 📄 Sample Output

# # # Each detected risk includes:

# # # - Severity
# # # - Category
# # # - Clause ID
# # # - Sentence ID
# # # - Trigger Source
# # # - Explanation
# # # - Matched Text
# # # - Clause Text
# # # - Risk Summary
# # # - Legal Consequence
# # # - Recommendation
# # # - Confidence Score

# # # ---

# # # ## 🎯 Project Goals

# # # This project was developed to demonstrate:

# # # - AI integration in real-world software
# # # - Rule-based NLP systems
# # # - Large Language Model integration
# # # - REST API development with FastAPI
# # # - Modern React frontend development
# # # - Clean software architecture
# # # - Professional UI/UX design
# # # - Resume-quality full-stack engineering

# # # ---

# # # ## 📌 Project Status

# # # ✅ Completed

# # # 🚀 Deployed

# # # 🎓 Portfolio Project


# # # ## 🔮 Future Improvements

# # # - Additional legal rule sets
# # # - Clause highlighting within uploaded documents
# # # - PDF export for analysis reports
# # # - Improved AI explanations
# # # - Dark mode
# # # - Deployment with Docker
# # # - Enhanced accessibility

# # # ---

# # # ## 📜 License

# # # This project is licensed under the MIT License.

# # # ---

# # # ## 👨‍💻 Author

# # # **Adarsh Sharma**

# # # Computer Science Engineering Student

# # # Built as a portfolio project to demonstrate AI-powered software engineering, modern frontend development, and backend integration using FastAPI, LangChain, and Google Gemini.



# # # RED FLAG — AI-Powered Legal Contract Risk Analyzer

# # ## Developer Architecture & Technical Documentation

# # ---

# # # Overview

# # RED FLAG is an AI-powered legal contract analysis system designed to assist users in understanding potentially risky clauses hidden inside legal documents such as Terms of Service, Rental Agreements, Employment Contracts, Privacy Policies, Software Licenses, NDAs, Service Agreements, and other text-heavy legal documents.

# # The objective of the project is **not** to replace legal professionals. Instead, the system acts as an intelligent first-pass reviewer that identifies clauses likely to contain legal risks and explains them in plain English. This allows users to understand contracts before agreeing to them and enables faster document review.

# # Unlike simple keyword-based scanners, RED FLAG combines deterministic rule-based analysis with Large Language Models (LLMs) to provide context-aware explanations while maintaining consistent outputs through structured schemas.

# # The project demonstrates modern AI engineering concepts including:

# # * Retrieval and document preprocessing
# # * Natural Language Processing
# # * Large Language Model orchestration
# # * Prompt engineering
# # * Structured AI outputs
# # * Backend API development
# # * Production-style software architecture
# # * Explainable AI
# # * Modular software engineering

# # ---

# # # Motivation

# # Legal contracts are intentionally detailed and often difficult for non-lawyers to understand.

# # Users commonly agree to:

# # * Terms and Conditions
# # * Privacy Policies
# # * Rental Agreements
# # * Employment Contracts
# # * Service Agreements

# # without reading them because they are long, repetitive, and written in complex legal language.

# # RED FLAG was built to reduce this information gap.

# # Instead of summarizing the document, the system highlights clauses that deserve attention and explains:

# # * Why the clause may be risky
# # * What legal consequence it could have
# # * How severe the issue is
# # * Recommended actions before accepting the agreement

# # ---

# # # High Level Architecture

# # ```
# #                 User Uploads Contract
# #                         │
# #                         ▼
# #                 FastAPI Upload Endpoint
# #                         │
# #                         ▼
# #                Document Type Detection
# #                         │
# #                         ▼
# #                Document Loader Pipeline
# #           (PDF / DOCX / TXT Supported)
# #                         │
# #                         ▼
# #                Text Cleaning Pipeline
# #                         │
# #                         ▼
# #               Clause Extraction Engine
# #                         │
# #                         ▼
# #               Risk Detection Pipeline
# #       (Rules + Prompt Engine + LLM)
# #                         │
# #                         ▼
# #             Structured JSON Generation
# #                         │
# #                         ▼
# #                  REST API Response
# #                         │
# #                         ▼
# #                React Frontend Display
# # ```

# # ---

# # # Technology Stack

# # ## Backend

# # * Python
# # * FastAPI
# # * LangChain
# # * Google Gemini
# # * Pydantic
# # * Uvicorn

# # ---

# # ## Frontend

# # * React
# # * JavaScript
# # * Tailwind CSS
# # * Vite

# # ---

# # ## AI Components

# # * Prompt Engineering
# # * Rule-Based Risk Detection
# # * Context-aware LLM Analysis
# # * Structured JSON Parsing
# # * Confidence Estimation

# # ---

# # # Project Structure

# # ```
# # backend/

# # app/

# # api/
# #     upload.py
# #     analyze.py

# # schemas/
# #     document.py
# #     response.py

# # services/

# # document/
# #     loader.py
# #     cleaner.py
# #     splitter.py

# # analysis/
# #     analyzer.py
# #     classifier.py
# #     prompt_builder.py

# # utils/
# #     helpers.py

# # main.py

# # frontend/

# # src/

# # components/

# # UploadPage
# # LoadingScreen
# # ResultsPage

# # App.jsx
# # ```

# # The project follows a modular architecture where every component performs a single responsibility.

# # ---

# # # Request Lifecycle

# # ## Step 1 — Upload

# # The client uploads a document through the frontend.

# # Supported formats include:

# # * PDF
# # * DOCX
# # * TXT

# # The backend validates:

# # * File extension
# # * File size
# # * Encoding
# # * Upload integrity

# # ---

# # ## Step 2 — Document Loading

# # Different loaders are responsible for reading different document formats.

# # Each loader converts its respective file into normalized plain text while preserving the logical order of the original document.

# # ---

# # ## Step 3 — Cleaning

# # The cleaning pipeline removes:

# # * duplicate whitespace
# # * broken formatting
# # * repeated page headers
# # * unnecessary line breaks
# # * invalid characters

# # The objective is to produce high-quality text for downstream AI processing.

# # ---

# # ## Step 4 — Clause Segmentation

# # Rather than treating an entire contract as one prompt, the system separates it into meaningful clauses.

# # Examples:

# # * Payment Terms
# # * Liability
# # * Arbitration
# # * Intellectual Property
# # * Privacy
# # * Automatic Renewal
# # * Termination
# # * Governing Law

# # This significantly improves analysis accuracy.

# # ---

# # # Why Clause-Based Analysis?

# # Large language models perform better on focused contexts.

# # Instead of analyzing:

# # ```
# # Entire 25-page contract
# # ```

# # RED FLAG analyzes:

# # ```
# # Clause 1

# # ↓

# # Clause 2

# # ↓

# # Clause 3

# # ↓

# # ...
# # ```

# # Benefits include:

# # * Lower token usage
# # * Better explanations
# # * Higher consistency
# # * Easier debugging
# # * Better scalability

# # ---

# # # Risk Detection Pipeline

# # Each clause enters a multi-stage pipeline.

# # Stage 1

# # Basic validation

# # ↓

# # Stage 2

# # Rule Matching

# # ↓

# # Stage 3

# # Prompt Generation

# # ↓

# # Stage 4

# # LLM Analysis

# # ↓

# # Stage 5

# # Structured Parsing

# # ↓

# # Stage 6

# # Confidence Scoring

# # ↓

# # Stage 7

# # JSON Response

# # ---

# # # Rule-Based Detection

# # The rule engine identifies clauses containing patterns associated with legal risks.

# # Examples include:

# # * Unlimited liability
# # * Automatic renewals
# # * One-sided termination
# # * Forced arbitration
# # * Mandatory jurisdiction
# # * Data collection
# # * Data sharing
# # * Intellectual property transfer
# # * Broad indemnification
# # * Waiver of legal rights
# # * Restrictive employment clauses

# # The rules act as the first filtering layer before invoking AI reasoning.

# # ---

# # # Prompt Engineering

# # Instead of asking generic questions, RED FLAG constructs structured prompts.

# # Each prompt asks the LLM to determine:

# # * Whether the clause contains legal risk
# # * Risk category
# # * Severity
# # * Explanation
# # * Legal implication
# # * Suggested action
# # * Confidence score

# # This dramatically improves consistency.

# # ---

# # # Structured Outputs

# # The model is instructed to return structured JSON.

# # Example fields include:

# # ```
# # severity

# # risk_summary

# # legal_consequence

# # recommendation

# # confidence
# # ```

# # Using structured outputs makes downstream processing significantly easier compared to parsing free-form text.

# # ---

# # # Severity Classification

# # Each identified clause is classified into one of three categories.

# # LOW

# # Minor concern or informational notice.

# # MEDIUM

# # Potentially unfavorable clause that should be reviewed.

# # HIGH

# # Significant legal concern that could materially affect the user.

# # ---

# # # Confidence Score

# # Every prediction includes a confidence value.

# # Purpose:

# # * Communicate uncertainty
# # * Improve transparency
# # * Enable future ranking
# # * Allow filtering in the frontend

# # ---

# # # Explainability

# # One of the main objectives of RED FLAG is explainability.

# # Instead of only stating:

# # "This clause is risky."

# # The system explains:

# # * why
# # * how
# # * possible consequences
# # * recommended next steps

# # This makes the output understandable even for non-technical users.

# # ---

# # # API Design

# # The backend exposes REST APIs.

# # Primary workflow:

# # ```
# # POST /upload

# # ↓

# # Analyze document

# # ↓

# # Return structured JSON
# # ```

# # The API remains stateless.

# # Each request contains all required information for processing.

# # ---

# # # Response Schema

# # Each detected risk contains:

# # ```
# # Clause

# # Severity

# # Summary

# # Legal Consequence

# # Recommendation

# # Confidence
# # ```

# # This schema keeps frontend rendering independent of the AI implementation.

# # ---

# # # Error Handling

# # The backend handles:

# # * Invalid files
# # * Unsupported formats
# # * Empty documents
# # * AI failures
# # * Parsing failures
# # * Timeout errors
# # * Validation errors

# # Meaningful error messages are returned to the client.

# # ---

# # # Scalability Considerations

# # Although RED FLAG is primarily a portfolio project, the architecture was designed with scalability in mind.

# # Possible improvements include:

# # * Asynchronous processing
# # * Background workers
# # * Redis queues
# # * Vector search
# # * Persistent document storage
# # * Multi-user authentication
# # * Audit logging
# # * Caching
# # * Incremental analysis

# # ---

# # # Security Considerations

# # The project follows several secure design principles.

# # Uploaded files are:

# # * validated
# # * parsed safely
# # * processed in memory where possible

# # Future production improvements could include:

# # * authentication
# # * encrypted storage
# # * malware scanning
# # * rate limiting
# # * API keys
# # * HTTPS enforcement

# # ---

# # # Design Principles

# # The system follows:

# # Single Responsibility Principle

# # Each module performs one task.

# # Modularity

# # Independent services reduce coupling.

# # Maintainability

# # Features can be extended without modifying unrelated modules.

# # Explainability

# # Every prediction includes human-readable reasoning.

# # Extensibility

# # New document types, AI models, and rule sets can be integrated with minimal changes.

# # ---

# # # Future Improvements

# # Potential future work includes:

# # * Multi-language contracts
# # * OCR support
# # * Clause similarity search
# # * Risk heatmaps
# # * Interactive document annotations
# # * Citation of relevant legal precedents
# # * User feedback loop
# # * Fine-tuned legal language models
# # * Semantic search using vector databases
# # * RAG-based legal knowledge retrieval
# # * Batch document processing
# # * Enterprise dashboard
# # * User authentication
# # * Exportable PDF reports

# # ---

# # # Learning Outcomes

# # This project demonstrates practical experience with:

# # * AI application development
# # * Backend engineering
# # * REST API design
# # * Prompt engineering
# # * Large Language Models
# # * LangChain orchestration
# # * Structured AI outputs
# # * Software architecture
# # * Modular Python development
# # * React frontend integration
# # * Explainable AI
# # * Error handling
# # * Data validation
# # * Production-style project organization

# # ---

# # # Conclusion

# # RED FLAG showcases how modern AI systems can combine deterministic logic with Large Language Models to solve a real-world problem. By integrating document preprocessing, modular backend services, rule-based analysis, prompt engineering, and structured AI outputs, the project provides an explainable and user-friendly approach to legal contract review.

# # Beyond identifying risky clauses, the project emphasizes transparency, maintainability, and extensibility—qualities that are essential in production AI systems. While designed as a portfolio project, the underlying architecture reflects patterns commonly used in industry-grade AI applications and provides a strong foundation for future enhancements such as Retrieval-Augmented Generation (RAG), semantic search, multilingual support, and enterprise-scale document processing.


# # RED FLAG — AI-Powered Legal Contract Risk Analyzer

# ## Developer Architecture & Technical Documentation
