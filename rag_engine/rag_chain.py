import os
from typing import Dict
from rag_engine.pdf_utils import pdf_extract, pdf_chunk
from rag_engine.vector_store import create_vector_store, load_vector_store
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

from langchain_core.documents import Document

def retrieve_context(db, query: str):
    retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 2})
    return retriever.invoke(query)

def build_context(relevant_chunks: list) -> str:
    return "\n\n".join([chunk.page_content for chunk in relevant_chunks])

def get_context(inputs: Dict[str, str]) -> Dict[str, str]:
    pdf_path, query, db_path = inputs["pdf_path"], inputs["query"], inputs["db_path"]

    if not os.path.exists(db_path):
        pdf_text = pdf_extract(pdf_path)
        chunks = pdf_chunk(pdf_text)
        db = create_vector_store(chunks, db_path)
    else:
        db = load_vector_store(db_path)

    relevant_chunks = retrieve_context(db, query)
    context = build_context(relevant_chunks)
    return {"context": context, "query": query}

# Setup RAG Chain
template = """You are an AI trained for question answering based on given context.

Question: {query}

Context: {context}

If the answer is not in the context, respond: 'The answer is not available.'
"""

rag_prompt = ChatPromptTemplate.from_template(template)
llm = ChatOpenAI(model="gpt-4o-mini")
output_parser = StrOutputParser()

rag_chain = RunnableLambda(get_context) | rag_prompt | llm | output_parser
