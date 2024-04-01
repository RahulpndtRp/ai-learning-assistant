from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List

def pdf_extract(pdf_path: str) -> List:
    loader = PyPDFLoader(pdf_path)
    return loader.load()

def pdf_chunk(pdf_text: List) -> List:
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    return text_splitter.split_documents(pdf_text)
