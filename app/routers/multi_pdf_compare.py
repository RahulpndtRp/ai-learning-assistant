from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse
import os
import shutil
from projects.multi_pdf_compare.multi_rag_chain import multi_pdf_compare_chain

router = APIRouter()

UPLOAD_FOLDER = "uploads/pdfs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@router.post("/query")
async def multi_pdf_query(file1: UploadFile = File(...), file2: UploadFile = File(...), query: str = Form(...)):
    pdf1_path = os.path.join(UPLOAD_FOLDER, file1.filename)
    pdf2_path = os.path.join(UPLOAD_FOLDER, file2.filename)

    with open(pdf1_path, "wb") as buffer:
        shutil.copyfileobj(file1.file, buffer)

    with open(pdf2_path, "wb") as buffer:
        shutil.copyfileobj(file2.file, buffer)

    result = multi_pdf_compare_chain({
        "pdf1_path": pdf1_path,
        "pdf2_path": pdf2_path,
        "query": query
    })

    return JSONResponse(content=result)
