import os
from typing import List
from langchain_community.document_loaders import YoutubeLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from projects.youtube_summarizer.schemas import YouTubeSummarizerRequest, YouTubeSummarizerResponse
from langchain.schema import Document

# Utility functions

def yt_transcript(video_url: str) -> List[Document]:
    loader = YoutubeLoader.from_youtube_url(video_url)
    transcript = loader.load()
    return transcript

def yt_chunk(transcript: List[Document]) -> List[Document]:
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = text_splitter.split_documents(transcript)
    return chunks

def create_vector_store(chunks: List[Document], db_path: str) -> Chroma:
    embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")
    db = Chroma.from_documents(documents=chunks, embedding=embedding_model, persist_directory=db_path)
    return db

def retrieve_context(db: Chroma, query: str) -> List[Document]:
    retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 2})
    relevant_chunks = retriever.invoke(query)
    return relevant_chunks

def build_context(relevant_chunks: List[Document]) -> str:
    context = "\n\n".join([chunk.page_content for chunk in relevant_chunks])
    return context

# Main function

def generate_answer(request: YouTubeSummarizerRequest) -> YouTubeSummarizerResponse:
    video_url = request.video_url
    query = request.query

    current_dir = os.getcwd()
    db_path = os.path.join(current_dir, "db", "chroma_db_yt")

    if not os.path.exists(db_path):
        transcript = yt_transcript(video_url)
        chunks = yt_chunk(transcript)
        db = create_vector_store(chunks, db_path)
    else:
        embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")
        db = Chroma(persist_directory=db_path, embedding_function=embedding_model)

    relevant_chunks = retrieve_context(db, query)
    context = build_context(relevant_chunks)

    # Build RAG chain
    template = """
    You are an AI model trained for question answering. You should answer the
    given question based on the given context only.

    Question : {query}

    Context : {context}

    If the answer is not present in the given context, respond as: 
    "The answer to this question is not available in the provided content."
    """
    rag_prompt = ChatPromptTemplate.from_template(template)
    llm = ChatOpenAI(model='gpt-4o-mini')
    str_parser = StrOutputParser()

    rag_chain = (
        RunnableLambda(lambda x: {'query': query, 'context': context})
        | rag_prompt
        | llm
        | str_parser
    )

    answer = rag_chain.invoke({'video_url': video_url, 'query': query, 'db_path': db_path})

    return YouTubeSummarizerResponse(answer=answer)
