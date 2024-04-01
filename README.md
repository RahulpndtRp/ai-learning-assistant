# AI Learning Assistant - PDF RAG Question Answering

This is a modular FastAPI project that implements a simple Retrieval-Augmented Generation (RAG) system over a PDF document.

## Features
- Upload a PDF file
- Extract and chunk the PDF content
- Create a vector store using OpenAI embeddings
- Retrieve relevant chunks based on query
- Use LLM (GPT-4o-mini) to answer based on retrieved context

## Setup Instructions
1. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
2. Run server:
    ```
    uvicorn app.main:app --reload
    ```
3. API Endpoint:
    - `POST /rag_query`
    - Form-Data:
        - `file`: PDF file
        - `query`: Query string

## Folder Structure
