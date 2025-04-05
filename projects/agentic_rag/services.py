# services.py

from crewai import Crew
from .constants import WEBSITE_URL, OPENAI_EMBEDDING_MODEL, OPENAI_LLM_MODEL
from .agents import (
    create_rewrite_agent, create_router_agent,
    create_retriever_agent, create_evaluator_agent,
    create_answer_agent
)
from .tasks import (
    create_rewrite_task, create_router_task,
    create_retriever_task, create_evaluator_task,
    create_answer_task
)
from langchain_community.tools import DuckDuckGoSearchResults
from typing import Type, Any
from crewai_tools import WebsiteSearchTool
from pydantic import BaseModel
from crewai.tools import BaseTool

class DuckDuckGoSearchInput(BaseModel):
    query: str

class DuckDuckGoSearchTool(BaseTool):
    name: str = "DuckDuckGo Search"
    description: str = "Searches the web using DuckDuckGo for the provided query."
    args_schema: Type[BaseModel] = DuckDuckGoSearchInput

    def _run(self, query: str) -> Any:
        search = DuckDuckGoSearchResults(output_format="list")
        return search.run(query)

class AgenticRAGService:
    def __init__(self):
        self.website_search_tool = WebsiteSearchTool(
            website=WEBSITE_URL,
            config=dict(
                llm=dict(provider="openai", config=dict(model=OPENAI_LLM_MODEL)),
                embedder=dict(provider="openai", config=dict(model=OPENAI_EMBEDDING_MODEL)),
            )
        )
        self.web_search_tool = DuckDuckGoSearchTool()

    def kickoff_agentic_rag(self, query: str) -> str:
        rewrite_agent = create_rewrite_agent()
        router_agent = create_router_agent()
        retriever_agent = create_retriever_agent(tools=[self.website_search_tool, self.web_search_tool])
        evaluator_agent = create_evaluator_agent()
        answer_agent = create_answer_agent()

        rewrite_task = create_rewrite_task(rewrite_agent)
        router_task = create_router_task(router_agent, [rewrite_task])
        retriever_task = create_retriever_task(retriever_agent, [rewrite_task, router_task])
        evaluator_task = create_evaluator_task(evaluator_agent, [rewrite_task, retriever_task])
        answer_task = create_answer_task(answer_agent, [rewrite_task, retriever_task, evaluator_task])

        crew = Crew(
            agents=[rewrite_agent, router_agent, retriever_agent, evaluator_agent, answer_agent],
            tasks=[rewrite_task, router_task, retriever_task, evaluator_task, answer_task],
            verbose=True
        )
        result = crew.kickoff(inputs={"query": query})
        return result
