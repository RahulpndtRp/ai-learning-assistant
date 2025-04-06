# services.py

from projects.llm_evaluation.llm_evaluator import LLMHallucinationEvaluator
from projects.llm_evaluation.deepeval_evaluator import DeepEvalEvaluator
from projects.llm_evaluation.ragas_evaluator import RAGASEvaluator
import asyncio


class LLMEvaluationService:
    def __init__(self):
        self.llm_evaluator = LLMHallucinationEvaluator()
        self.deepeval_evaluator = DeepEvalEvaluator()
        self.ragas_evaluator = RAGASEvaluator()

    def detect_hallucination_llm(self, context: list, question: str, answer: str):
        full_context = " ".join(context)
        result = self.llm_evaluator.evaluate(full_context, question, answer)
        return result

    def evaluate_with_deepeval(self, query: str, context: list, response: str, reference: str):
        results = self.deepeval_evaluator.evaluate(query, context, response, reference)
        return results

    async def evaluate_with_ragas(self, query: str, context: list, response: str, reference: str):
        results = await self.ragas_evaluator.evaluate(query, context, response, reference)
        return results
