# llm_evaluation_router.py

from fastapi import APIRouter
from projects.llm_evaluation.services import LLMEvaluationService
from projects.llm_evaluation.schemas import (
    HallucinationDetectionRequest,
    HallucinationDetectionResponse,
    DeepEvalResponse,
    RAGASResponse
)

router = APIRouter()

evaluation_service = LLMEvaluationService()


@router.post("/llm-evaluator", response_model=HallucinationDetectionResponse)
async def detect_hallucination(request: HallucinationDetectionRequest):
    """Detect hallucination in an answer using LLM-based evaluation."""
    result = evaluation_service.detect_hallucination_llm(
        context=request.context,
        question=request.question,
        answer=request.answer
    )
    return result


@router.post("/deepeval-evaluator", response_model=DeepEvalResponse)
async def evaluate_with_deepeval(request: HallucinationDetectionRequest):
    """Evaluate RAG quality using DeepEval framework metrics."""
    results = evaluation_service.evaluate_with_deepeval(
        query=request.question,
        context=request.context,
        response=request.answer,
        reference=request.answer
    )
    return results


@router.post("/ragas-evaluator", response_model=RAGASResponse)
async def evaluate_with_ragas(request: HallucinationDetectionRequest):
    """Evaluate RAG quality using RAGAS framework metrics."""
    results = await evaluation_service.evaluate_with_ragas(
        query=request.question,
        context=request.context,
        response=request.answer,
        reference=request.answer
    )
    return results
