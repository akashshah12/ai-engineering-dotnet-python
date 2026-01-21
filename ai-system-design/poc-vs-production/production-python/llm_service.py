from openai import OpenAI
from config import MODEL_NAME
from logging_setup import logger
from functools import lru_cache

client = OpenAI()

@lru_cache(maxsize=1000)
def ask_ai_cached(question: str) -> str:
    if not question or len(question) > 500:
        raise ValueError("Invalid input")

    logger.info("Sending request to LLM")

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": question}]
    )

    logger.info("Received response from LLM")

    return response.choices[0].message.content
	
	
/*

✅ Improvements

Input validation

Centralized config

Logging hooks

Service abstraction

Ready for retries, metrics, caching

*/
