from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse
import os
import shutil
from projects.single_pdf_rag.rag_chain import single_pdf_rag_chain

router = APIRouter()

UPLOAD_FOLDER = "uploads/pdfs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@router.post("/query")
async def single_pdf_query(file: UploadFile = File(...), query: str = Form(...)):
    pdf_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(pdf_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = single_pdf_rag_chain({
        "pdf_path": pdf_path,
        "query": query
    })

    return JSONResponse(content=result)
