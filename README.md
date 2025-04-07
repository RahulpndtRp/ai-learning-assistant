# AI Learning Assistant

A collection of small, useful Machine Learning and GenAI applications built with FastAPI.  
Designed with a modular and scalable architecture for easy expansion and maintenance.

---

## 🚀 Available Projects

| Project Name                     | API Prefix               | Description                                                       |
|:---------------------------------|:-------------------------|:------------------------------------------------------------------|
| **Single PDF RAG**               | `/pdf-rag`               | Retrieve information from a single PDF using Retrieval-Augmented Generation (RAG) with LangChain. |
| **Multi PDF Comparison**         | `/multi-pdf-compare`     | Compare and answer questions across multiple PDFs using a Multi-RAG Chain setup. |
| **YouTube Video Summarizer**     | `/youtube-rag`           | Summarize YouTube videos by extracting transcripts and generating answers based on context. |
| **Web Page Summarizer**          | `/webpage-rag`           | Summarize content from web pages and answer queries using a RAG pipeline. |
| **Agentic RAG with CrewAI**      | `/agentic-rag`           | Multi-agent RAG system using CrewAI, with intelligent query rewriting, routing, retrieval, evaluation, and answering. |
| **LLM Evaluation**               | `/llm-evaluation`        | Hallucination detection and RAG evaluation via ChatGPT, DeepEval, and RAGAS frameworks. |

---

## 🏗 Project Structure

```
common_sdk/
├── logger.py            # Centralized logger
├── exception_handler.py # Global exception handlers
├── tracing.py           # Request ID middleware
└── validators.py        # Shared validation utilities

app/
├── main.py              # FastAPI app entry
├── routers/             # API routers
│   ├── single_pdf_rag.py
│   ├── multi_pdf_compare.py
│   ├── youtube_router.py
│   ├── webpage_router.py
│   ├── agentic_rag_router.py
│   └── llm_evaluation_router.py
projects/
├── single_pdf_rag/      # Single PDF RAG logic
├── multi_pdf_compare/   # Multi PDF comparison logic
├── youtube_summarizer/  # YouTube RAG logic
├── webpage_summarizer/  # Web Page RAG logic
├── agentic_rag/         # CrewAI Agentic RAG logic
└── llm_evaluation/      # Hallucination & RAG evaluation logic

uploads/
├── db/
└── pdfs/

```

---

## 📦 Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/ai-learning-assistant.git
   cd ai-learning-assistant
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate    # Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🔧 Running the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Visit the Swagger UI at: `http://127.0.0.1:8000/docs`

---

## 📝 Common SDK Features

- **Centralized Logging**  
  Located in `common_sdk/logger.py`. Use `get_logger(__name__)` to obtain a structured logger.

- **Global Exception Handling**  
  Defined in `common_sdk/exception_handler.py`. Automatically handles `HTTPException` and unexpected `Exception` to return clean JSON errors.

- **Request Tracing**  
  Middleware in `common_sdk/tracing.py` generates a unique `X-Request-ID` for each request, included in logs and response headers.

- **Shared Validators**  
  Utility functions in `common_sdk/validators.py` for common Pydantic validation (e.g., non-empty lists).

---

## 🛠 API Endpoints Summary

| Method | Endpoint                      | Description                                             |
|:-------|:------------------------------|:--------------------------------------------------------|
| POST    | `/pdf-rag/query`             | Single PDF RAG query                                   |
| POST    | `/multi-pdf-compare/query`   | Multiple PDF comparison query                          |
| POST    | `/youtube-rag/query`         | YouTube video summarization                            |
| POST    | `/webpage-rag/query`         | Web page summarization                                 |
| POST    | `/agentic-rag/query`         | Agentic RAG multi-agent workflow                       |
| POST    | `/llm-evaluation/llm-evaluator`    | LLM-based hallucination detection                     |
| POST    | `/llm-evaluation/deepeval-evaluator` | DeepEval framework RAG evaluation                    |
| POST    | `/llm-evaluation/ragas-evaluator`   | RAGAS framework RAG evaluation                       |

---

## 🛡 Error Handling & Logging

- All API exceptions are caught and returned as JSON with proper HTTP status codes.
- Logs include timestamps, log level, module name, message, and request IDs for traceability.

---

## 🙌 Contributing

Feel free to fork, submit issues, or open pull requests.  
For major changes, please open an issue first to discuss what you would like to change.

---

## 📜 License

MIT License. See `LICENSE` for details.
