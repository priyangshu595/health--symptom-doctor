from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json
import re
import os

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔑 Replace with your OpenRouter API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

class SymptomInput(BaseModel):
    symptoms: str

@app.post("/analyze")
def analyze_symptoms(data: SymptomInput):

    # 🔥 Improved prompt (structured + concise)
    prompt = f"""
    You are a medical assistant (educational use only).

    Given symptoms: {data.symptoms}

    Return STRICTLY in this JSON format:

    {{
      "conditions": ["condition1", "condition2"],
      "severity": "Low/Medium/High",
      "recommendations": ["step1", "step2"],
      "doctor_visit": "When to consult doctor",
      "disclaimer": "This is not a medical diagnosis"
    }}

    Keep answers concise and relevant.
    Avoid long explanations.
    """

    try:
        # 🔗 API call to OpenRouter
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "meta-llama/llama-3-8b-instruct",  # ✅ best free model
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.3  # 🔥 more stable output
            }
        )

        result = response.json()

        # 🔍 Extract model output
        content = result['choices'][0]['message']['content']

        # 🧠 Try parsing JSON output
        try:
            json_str = re.search(r'\{.*\}', content, re.DOTALL).group()
            structured_output = json.loads(json_str)
            return structured_output
        except:
            # fallback if model returns text instead of JSON
            return {
               "analysis": content,
               "note": "Output not in JSON format"
    }

    except Exception as e:
        return {
            "error": str(e)
        }