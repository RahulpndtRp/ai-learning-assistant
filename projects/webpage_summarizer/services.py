import os
from typing import Dict
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain.schema import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

# Extract text from web page
def wp_text(page_url: str) -> list[Document]:
    print("Web page text is extracted...")
    loader = WebBaseLoader(page_url)
    webpage_text = loader.load()
    return webpage_text

# Chunk the text
def wp_chunk(webpage_text: list[Document]) -> list[Document]:
    print("Web page text is chunked...")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = text_splitter.split_documents(webpage_text)
    return chunks

# Create Vector Store
def create_vector_store(chunks: list[Document], db_path: str) -> Chroma:
    print("Chroma vector store is created...\n")
    embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")
    db = Chroma.from_documents(documents=chunks, embedding=embedding_model, persist_directory=db_path)
    return db

# Retrieve Context
def retrieve_context(db: Chroma, query: str) -> list[Document]:
    retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 2})
    print("Relevant chunks are retrieved...\n")
    relevant_chunks = retriever.invoke(query)
    return relevant_chunks

# Build Context
def build_context(relevant_chunks: list[Document]) -> str:
    print("Context is built from relevant chunks")
    context = "\n\n".join([chunk.page_content for chunk in relevant_chunks])
    return context

# Full Context Builder
def get_context(inputs: Dict[str, str]) -> Dict[str, str]:
    page_url, query = inputs["page_url"], inputs["query"]
    db_path = os.path.join("db", "chroma_db_wp")

    if not os.path.exists(db_path):
        os.makedirs(db_path, exist_ok=True)
        print("Creating a new vector store...\n")
        webpage_text = wp_text(page_url)
        chunks = wp_chunk(webpage_text)
        db = create_vector_store(chunks, db_path)
    else:
        print("Loading the existing vector store...\n")
        embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")
        db = Chroma(persist_directory=db_path, embedding_function=embedding_model)

    relevant_chunks = retrieve_context(db, query)
    context = build_context(relevant_chunks)
    return {"context": context, "query": query}

# RAG Chain
template = """
You are an AI model trained for question answering.
You should answer the given question based on the given context only.

Question: {query}

Context: {context}

If the answer is not present in the given context, respond as:
"The answer to this question is not available in the provided content."
"""

rag_prompt = ChatPromptTemplate.from_template(template)
llm = ChatOpenAI(model="gpt-4o-mini")
str_parser = StrOutputParser()

rag_chain = (
    RunnableLambda(get_context)
    | rag_prompt
    | llm
    | str_parser
)
