from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
import os
import shutil
from rag_engine.rag_chain import rag_chain
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
app = FastAPI()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/rag_query")
async def rag_query(file: UploadFile = File(...), query: str = Form(...)):
    temp_file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    db_path = os.path.join(UPLOAD_FOLDER, "chroma_db_pdf")

    result = rag_chain.invoke({
        "pdf_path": temp_file_path,
        "query": query,
        "db_path": db_path
    })

    return JSONResponse(content={"query": query, "answer": result})
