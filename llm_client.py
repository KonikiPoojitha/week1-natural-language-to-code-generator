import os
from typing import Optional

SYSTEM_PROMPT = """You are a Python code generator.
Convert the user's plain-English programming task into correct, runnable Python code.
Return ONLY Python code.
Do NOT return explanations.
Do NOT use Markdown code fences.
Do NOT add introductory or concluding text.
Prefer simple, readable Python suitable for a beginner.
Include a small example or __main__ block only when it helps demonstrate the requested task.
"""


def _groq_generate(task: str) -> str:
    from groq import Groq

    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY is not set.")

    model = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")
    client = Groq(api_key=api_key)

    response = client.chat.completions.create(
        model=model,
        temperature=0.1,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": task},
        ],
    )
    return response.choices[0].message.content or ""


def _ollama_generate(task: str) -> str:
    import requests

    model = os.getenv("OLLAMA_MODEL", "llama3.2")
    url = os.getenv("OLLAMA_URL", "http://localhost:11434/api/chat")

    response = requests.post(
        url,
        json={
            "model": model,
            "stream": False,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": task},
            ],
        },
        timeout=120,
    )
    response.raise_for_status()
    data = response.json()
    return data["message"]["content"]


def generate_code(task: str, provider: Optional[str] = None) -> str:
    provider = (provider or os.getenv("LLM_PROVIDER", "groq")).lower()

    if provider == "groq":
        return _groq_generate(task)
    if provider == "ollama":
        return _ollama_generate(task)

    raise ValueError("LLM_PROVIDER must be 'groq' or 'ollama'.")
