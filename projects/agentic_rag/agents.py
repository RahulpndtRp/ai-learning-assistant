# agents.py

from crewai import Agent, LLM
from .constants import OPENAI_LLM_MODEL

def get_llm():
    return LLM(model=OPENAI_LLM_MODEL)

def create_rewrite_agent():
    llm = get_llm()
    return Agent(
        role="Query Rewriting Specialist",
        goal="Analyze and improve search query for better results",
        backstory="Expert in NLP and search optimization.",
        llm=llm,
        allow_delegation=False,
        verbose=True
    )

def create_router_agent():
    llm = get_llm()
    return Agent(
        role="Traffic Router",
        goal="Determine the appropriate search destination",
        backstory="Specialized in routing based on query analysis.",
        llm=llm,
        allow_delegation=False,
        verbose=True
    )

def create_retriever_agent(tools):
    llm = get_llm()
    return Agent(
        role="Information Retriever",
        goal="Fetch relevant info from web or vector store",
        backstory="Expert at fast information retrieval.",
        llm=llm,
        tools=tools,
        allow_delegation=False,
        verbose=True
    )

def create_evaluator_agent():
    llm = get_llm()
    return Agent(
        role="Content Evaluator",
        goal="Assess the relevance of retrieved information",
        backstory="Skilled in content evaluation and relevance checking.",
        llm=llm,
        allow_delegation=False,
        verbose=True
    )

def create_answer_agent():
    llm = get_llm()
    return Agent(
        role="Response Generator",
        goal="Generate clear and concise answers",
        backstory="Expert at synthesizing information into user answers.",
        llm=llm,
        allow_delegation=False,
        verbose=True
    )
