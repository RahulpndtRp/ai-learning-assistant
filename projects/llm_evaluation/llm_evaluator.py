# llm_evaluator.py

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from projects.llm_evaluation.constants import OPENAI_LLM_MODEL, HALLUCINATION_PROMPT_TEMPLATE


class HallucinationResult(BaseModel):
    hallucination_detected: bool = Field(
        description="Whether a hallucination was detected in the answer"
    )
    hallucinated_text_span: str = Field(
        description="The specific hallucinated part of the answer, or empty if none"
    )
    details: str = Field(
        description="Explanation why the answer is hallucinated or correct"
    )


class LLMHallucinationEvaluator:
    def __init__(self):
        self.llm = ChatOpenAI(model=OPENAI_LLM_MODEL, temperature=0)
        self.output_parser = PydanticOutputParser(pydantic_object=HallucinationResult)
        self.chat_prompt = ChatPromptTemplate.from_template(HALLUCINATION_PROMPT_TEMPLATE)

        self.chain = self.chat_prompt | self.llm | self.output_parser

    def evaluate(self, context: str, question: str, answer: str) -> HallucinationResult:
        inputs = {
            "context": context,
            "question": question,
            "answer": answer,
            "format_instructions": self.output_parser.get_format_instructions()
        }
        result = self.chain.invoke(inputs)
        return result
