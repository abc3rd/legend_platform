# routes/generate_image.py

from fastapi import APIRouter
from pydantic import BaseModel
import requests
import os

router = APIRouter(prefix="/generate-image", tags=["Image Generation"])

class Prompt(BaseModel):
    prompt: str

REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")
HEADERS = {"Authorization": f"Token {REPLICATE_API_TOKEN}"}

@router.post("/")
async def generate_image(data: Prompt):
    try:
        payload = {
            "version": "db21e45a3cba295ed73f6e3e9c5b4099b7f79b0ec40cf42d6fca2c1d519f2e5c",
            "input": {
                "prompt": data.prompt
            }
        }
        response = requests.post(
            "https://api.replicate.com/v1/predictions",
            json=payload,
            headers=HEADERS
        )

        result = response.json()
        image_url = result["prediction"]["output"][0] if "prediction" in result and "output" in result["prediction"] else None

        return {
            "prompt": data.prompt,
            "image_url": image_url or "No image returned",
            "raw_response": result
        }

    except Exception as e:
        return {"error": str(e)}
