from projects.single_pdf_rag.pdf_utils import pdf_extract, pdf_chunk
from projects.single_pdf_rag.vector_store import create_vector_store, load_vector_store
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

DB_FOLDER = "uploads/db"
os.makedirs(DB_FOLDER, exist_ok=True)

def prepare_db(pdf_path: str, db_name: str):
    db_path = os.path.join(DB_FOLDER, db_name)
    if not os.path.exists(db_path):
        pdf_text = pdf_extract(pdf_path)
        chunks = pdf_chunk(pdf_text)
        db = create_vector_store(chunks, db_path)
    else:
        db = load_vector_store(db_path)
    return db

def ask_db(db, query):
    retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 2})
    relevant_chunks = retriever.invoke(query)
    context = "\n\n".join([chunk.page_content for chunk in relevant_chunks])

    template = """
    You are an AI model trained to answer based on provided document content.
    Question: {query}
    Context: {context}
    If the answer is not available, say: 'Answer not available.'
    """
    prompt = ChatPromptTemplate.from_template(template)
    llm = ChatOpenAI(model="gpt-4o-mini")
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

    return chain.invoke({"query": query, "context": context})

def multi_pdf_compare_chain(inputs: dict):
    pdf1_path = inputs["pdf1_path"]
    pdf2_path = inputs["pdf2_path"]
    query = inputs["query"]

    db1 = prepare_db(pdf1_path, db_name="db1")
    db2 = prepare_db(pdf2_path, db_name="db2")

    answer1 = ask_db(db1, query)
    answer2 = ask_db(db2, query)

    comparison = "Same Answer ✅" if answer1.strip() == answer2.strip() else "Different Answer 🚨"

    return {
        "query": query,
        "pdf1_answer": answer1,
        "pdf2_answer": answer2,
        "comparison_result": comparison
    }
