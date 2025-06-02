# routes/query.py

from fastapi import APIRouter, Request
from pydantic import BaseModel
import requests

router = APIRouter(prefix="/query", tags=["Query"])

class QueryInput(BaseModel):
    query: str

@router.post("/")
async def query_handler(data: QueryInput, request: Request):
    try:
        prompt = data.query

        # Send to local OpenHermes model via Ollama API
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "openhermes",
                "prompt": prompt,
                "stream": False
            }
        )

        output = response.json().get("response", "[No response returned]")
        return {
            "query": prompt,
            "response": output
        }

    except Exception as e:
        return {
            "error": str(e),
            "note": "Ensure Ollama is running and OpenHermes model is pulled"
        }














