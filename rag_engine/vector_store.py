import os
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

def create_vector_store(chunks, db_path: str) -> Chroma:
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    db = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory=db_path)
    return db

def load_vector_store(db_path: str) -> Chroma:
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    return Chroma(persist_directory=db_path, embedding_function=embeddings)
