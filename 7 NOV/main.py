from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests, os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

class Query(BaseModel):
    topic: str
    question: str

@app.post("/ask")
async def ask(query: Query):
    try:
        prompt = f"{query.topic}: {query.question}"
        headers = {
            "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost:8000",  # or your actual domain
            "X-Title": "AI Knowledge Assistant"
        }
        body = {
            "model": "mistralai/mistral-7b-instruct",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        }
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=body)

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)

        return {"response": response.json()["choices"][0]["message"]["content"]}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))