from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List
from langchain.schema import Document

def pdf_extract(pdf_path: str) -> List[Document]:
    loader = PyPDFLoader(pdf_path)
    pdf_text = loader.load()
    return pdf_text

def pdf_chunk(pdf_text: List[Document]) -> List[Document]:
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = text_splitter.split_documents(pdf_text)
    return chunks
