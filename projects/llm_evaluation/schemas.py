# schemas.py

from pydantic import BaseModel
from typing import List, Optional


class HallucinationDetectionRequest(BaseModel):
    context: List[str]
    question: str
    answer: str


class HallucinationDetectionResponse(BaseModel):
    hallucination_detected: bool
    hallucinated_text_span: Optional[str]
    details: Optional[str]


class MetricResult(BaseModel):
    score: float
    reason: Optional[str]


class DeepEvalResponse(BaseModel):
    context_precision: MetricResult
    context_recall: MetricResult
    faithfulness: MetricResult
    answer_relevancy: MetricResult
    hallucination: MetricResult


class RAGASResponse(BaseModel):
    context_precision: float
    context_recall: float
    context_entity_recall: float
    response_relevancy: float
    faithfulness: float
