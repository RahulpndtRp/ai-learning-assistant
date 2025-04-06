# constants.py

# OpenAI models
OPENAI_LLM_MODEL = "gpt-4o-mini"
OPENAI_EMBEDDING_MODEL = "text-embedding-3-small"

# LettuceDetect model path
LETTUCE_MODEL_PATH = "KRLabsOrg/lettucedect-base-modernbert-en-v1"

# Thresholds for evaluation metrics
DEEPEVAL_CONTEXT_PRECISION_THRESHOLD = 0.75
DEEPEVAL_CONTEXT_RECALL_THRESHOLD = 0.8
DEEPEVAL_FAITHFULNESS_THRESHOLD = 0.7
DEEPEVAL_ANSWER_RELEVANCY_THRESHOLD = 0.75
DEEPEVAL_HALLUCINATION_THRESHOLD = 0.6

# Prompt Template for Hallucination Detection (LLM based)
HALLUCINATION_PROMPT_TEMPLATE = """
You are an expert fact-checker tasked with detecting hallucinations (inaccurate or unsupported information) 
in answers based on provided context and question. A hallucination occurs when the answer contains information 
that contradicts the context, is not supported by it, or introduces extraneous details not asked for by the question.

Context: {context}
Question: {question}
Answer: {answer}

Your task is to:
1. Compare the answer to the context and question.
2. Identify any specific text spans in the answer that are hallucinatory (inaccurate or unsupported).
3. Provide a detailed explanation of your findings.

Please analyze and return the result in structured JSON format as per schema.
{format_instructions}
"""
