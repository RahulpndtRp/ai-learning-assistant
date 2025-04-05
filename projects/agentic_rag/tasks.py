# tasks.py

from crewai import Task

def create_rewrite_task(agent):
    return Task(
        description="Analyze and rewrite query {query} for better results if needed.",
        expected_output="A well-formed query or original query.",
        agent=agent
    )

def create_router_task(agent, context):
    return Task(
        description="Decide between 'vector_store' or 'web_search' based on query.",
        expected_output="Either 'vector_store' or 'web_search'.",
        agent=agent,
        context=context
    )

def create_retriever_task(agent, context):
    return Task(
        description="Retrieve relevant information based on router output.",
        expected_output="Relevant info from vector_store or web_search.",
        agent=agent,
        context=context
    )

def create_evaluator_task(agent, context):
    return Task(
        description="Evaluate if retrieved information is relevant and complete.",
        expected_output="'yes' or 'no'.",
        agent=agent,
        context=context
    )

def create_answer_task(agent, context):
    return Task(
        description="Generate final answer based on evaluation result.",
        expected_output="Final answer or 'Unable to answer the query'.",
        agent=agent,
        context=context
    )
