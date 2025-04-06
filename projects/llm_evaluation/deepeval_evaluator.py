# deepeval_evaluator.py

from deepeval.metrics import (
    ContextualPrecisionMetric,
    ContextualRecallMetric,
    FaithfulnessMetric,
    AnswerRelevancyMetric,
    HallucinationMetric
)
from deepeval.test_case import LLMTestCase
from projects.llm_evaluation.constants import (
    OPENAI_LLM_MODEL,
    DEEPEVAL_CONTEXT_PRECISION_THRESHOLD,
    DEEPEVAL_CONTEXT_RECALL_THRESHOLD,
    DEEPEVAL_FAITHFULNESS_THRESHOLD,
    DEEPEVAL_ANSWER_RELEVANCY_THRESHOLD,
    DEEPEVAL_HALLUCINATION_THRESHOLD
)

class DeepEvalEvaluator:
    def __init__(self):
        self.metrics = {
            "context_precision": ContextualPrecisionMetric(
                threshold=DEEPEVAL_CONTEXT_PRECISION_THRESHOLD,
                model=OPENAI_LLM_MODEL,
                include_reason=True
            ),
            "context_recall": ContextualRecallMetric(
                threshold=DEEPEVAL_CONTEXT_RECALL_THRESHOLD,
                model=OPENAI_LLM_MODEL,
                include_reason=True
            ),
            "faithfulness": FaithfulnessMetric(
                threshold=DEEPEVAL_FAITHFULNESS_THRESHOLD,
                model=OPENAI_LLM_MODEL,
                include_reason=True
            ),
            "answer_relevancy": AnswerRelevancyMetric(
                threshold=DEEPEVAL_ANSWER_RELEVANCY_THRESHOLD,
                model=OPENAI_LLM_MODEL,
                include_reason=True
            ),
            "hallucination": HallucinationMetric(
                threshold=DEEPEVAL_HALLUCINATION_THRESHOLD,
                model=OPENAI_LLM_MODEL,
                include_reason=True
            )
        }
    def evaluate(self, query: str, context: list, response: str, reference: str = None) -> dict:
        results = {}
        for name, metric in self.metrics.items():
            print(f"\nEvaluating Metric: {name}")
            print(f"Query: {query}")
            print(f"Response: {response}")
            print(f"Reference: {reference}")
            print(f"Context: {context}\n")

            if name in ["context_precision", "context_recall", "faithfulness"]:
                test_case = LLMTestCase(
                    input=query,
                    actual_output=response,
                    expected_output=reference,
                    retrieval_context=context
                )
            elif name == "hallucination":
                test_case = LLMTestCase(
                    input=query,
                    actual_output=response,
                    context=context,
                    retrieval_context=context
                )
            elif name == "answer_relevancy":
                test_case = LLMTestCase(
                    input=query,
                    actual_output=response
                )
            else:
                raise ValueError(f"Unknown metric: {name}")

            metric.measure(test_case)

            results[name] = {
                "score": metric.score,
                "reason": metric.reason
            }

        return results
