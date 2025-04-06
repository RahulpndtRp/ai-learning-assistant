# ragas_evaluator.py

import asyncio
from ragas.llms import LangchainLLMWrapper
from ragas import SingleTurnSample
from ragas.metrics import (
    LLMContextPrecisionWithReference,
    LLMContextRecall,
    ContextEntityRecall,
    ResponseRelevancy,
    Faithfulness
)
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from ragas.embeddings import LangchainEmbeddingsWrapper
from projects.llm_evaluation.constants import OPENAI_LLM_MODEL, OPENAI_EMBEDDING_MODEL


class RAGASEvaluator:
    def __init__(self):
        self.llm = ChatOpenAI(model=OPENAI_LLM_MODEL)
        self.evaluator_llm = LangchainLLMWrapper(self.llm)
        self.embeddings = LangchainEmbeddingsWrapper(OpenAIEmbeddings(model=OPENAI_EMBEDDING_MODEL))

        self.metrics = {
            "context_precision": LLMContextPrecisionWithReference(llm=self.evaluator_llm),
            "context_recall": LLMContextRecall(llm=self.evaluator_llm),
            "context_entity_recall": ContextEntityRecall(llm=self.evaluator_llm),
            "response_relevancy": ResponseRelevancy(llm=self.evaluator_llm, embeddings=self.embeddings),
            "faithfulness": Faithfulness(llm=self.evaluator_llm)
        }

    async def evaluate(self, query: str, context: list, response: str, reference: str) -> dict:
        sample = SingleTurnSample(
            user_input=query,
            reference=reference,
            response=response,
            retrieved_contexts=context
        )

        results = {}
        for name, metric in self.metrics.items():
            score = await metric.single_turn_ascore(sample)
            results[name] = score
        return results
