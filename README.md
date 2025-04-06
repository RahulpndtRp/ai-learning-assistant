
# AI Learning Assistant

A collection of small, useful Machine Learning and GenAI applications built with FastAPI.  
Designed with a modular and scalable architecture for easy expansion and maintenance.

---

## 🚀 Available Projects

| Project Name | API Prefix | Description |
|:-------------|:-----------|:------------|
| **Single PDF RAG** | `/pdf-rag` | Retrieve information from a single PDF using Retrieval-Augmented Generation (RAG) with LangChain. |
| **Multi PDF Comparison** | `/multi-pdf-compare` | Compare and answer questions across multiple PDFs using a Multi-RAG Chain setup. |
| **YouTube Video Summarizer** | `/youtube-rag` | Summarize YouTube videos by extracting transcripts and generating answers based on context. |
| **Web Page Summarizer** | `/webpage-rag` | Summarize content from web pages and answer queries using a RAG pipeline. |
| **Agentic RAG with CrewAI** | `/agentic-rag` | Multi-agent RAG system using CrewAI, with intelligent query rewriting, routing, retrieval, evaluation, and answering. |

---

## 🏗 Project Structure

```
app/
├── main.py          # FastAPI app entry point
├── routers/         # API routers (endpoints)
projects/
├── single_pdf_rag/  # Business logic for Single PDF RAG
├── multi_pdf_compare/
├── youtube_summarizer/
├── webpage_summarizer/
├── agentic_rag/
uploads/
├── pdfs/            # Upload folder for PDFs
├── db/              # Chroma DB storage
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

3. **Install requirements**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the FastAPI app**:
   ```bash
   uvicorn app.main:app --reload --loop asyncio
   ```

5. **Open the app**:
   - Visit: `http://127.0.0.1:8000/docs` (FastAPI Swagger UI)

---

## 🛠 API Endpoints Summary

| Method | Endpoint | Description |
|:-------|:---------|:------------|
| `POST` | `/pdf-rag/query` | Query Single PDF RAG |
| `POST` | `/multi-pdf-compare/query` | Query Multi PDF Comparison |
| `POST` | `/youtube-rag/query` | Query YouTube Video Summarizer |
| `POST` | `/webpage-rag/query` | Query Web Page Summarizer |
| `POST` | `/agentic-rag/query` | Query Agentic RAG Multi-Agent System |

---

## ✨ Tech Stack

- **FastAPI** — API backend
- **CrewAI** — Multi-agent orchestration
- **LangChain** — RAG chains
- **ChromaDB** — Vector store
- **DuckDuckGo Search** — Web search integration
- **Pydantic** — Request and response validation
- **OpenAI Models** — LLM and Embeddings

---

## 🙌 Contributions

This project is authored and maintained by **Rahul Pandey**.  
Feel free to fork, contribute, and build on top of this modular assistant!

