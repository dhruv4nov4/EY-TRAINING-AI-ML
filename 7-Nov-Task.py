# index.html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Q&A Assistant</title>
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      min-height: 100vh;
      margin: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }
    .container {
      max-width: 700px;
      width: 100%;
      background: #fff;
      border-radius: 15px;
      padding: 40px;
      box-shadow: 0 10px 40px rgba(0,0,0,0.2);
    }
    h1 {
      text-align: center;
      margin-bottom: 10px;
    }
    .subtitle {
      text-align: center;
      color: #666;
      margin-bottom: 30px;
    }
    textarea {
      width: 100%;
      padding: 15px;
      border: 2px solid #e0e0e0;
      border-radius: 8px;
      font-size: 16px;
      min-height: 120px;
      resize: vertical;
    }
    textarea:focus {
      outline: none;
      border-color: #667eea;
    }
    button {
      width: 100%;
      padding: 15px;
      margin-top: 15px;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: #fff;
      border: none;
      border-radius: 8px;
      font-size: 16px;
      font-weight: 600;
      cursor: pointer;
    }
    button:disabled {
      opacity: 0.6;
      cursor: not-allowed;
    }
    .response-box {
      margin-top: 30px;
      padding: 20px;
      background: #f8f9fa;
      border-left: 4px solid #667eea;
      border-radius: 8px;
      display: none;
    }
    .response-box.show {
      display: block;
    }
    .response-box.error {
      border-left-color: #dc3545;
      background: #ffe6e6;
      color: #dc3545;
    }
    .loading {
      text-align: center;
      margin-top: 20px;
      display: none;
      color: #667eea;
    }
    .loading.show {
      display: block;
    }
    .spinner {
      border: 3px solid #f3f3f3;
      border-top: 3px solid #667eea;
      border-radius: 50%;
      width: 40px;
      height: 40px;
      animation: spin 1s linear infinite;
      margin: 20px auto;
    }
    @keyframes spin {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>🤖 Ask Me Anything</h1>
    <p class="subtitle">Powered by your FastAPI backend</p>

    <form id="qaForm">
      <label for="question">Your Question:</label>
      <textarea id="question" placeholder="Type your question here..." required></textarea>
      <button type="submit" id="submitBtn"><span id="buttonText">Ask Question</span></button>
    </form>

    <div id="loading" class="loading">
      <div class="spinner"></div>
      <p>Thinking...</p>
    </div>

    <div id="responseBox" class="response-box">
      <h3>Answer:</h3>
      <p id="responseText"></p>
    </div>
  </div>

  <script>
    const API_URL = 'http://localhost:8000';

    document.getElementById('qaForm').addEventListener('submit', async (e) => {
      e.preventDefault();

      const question = document.getElementById('question').value.trim();
      const submitBtn = document.getElementById('submitBtn');
      const buttonText = document.getElementById('buttonText');
      const loading = document.getElementById('loading');
      const responseBox = document.getElementById('responseBox');
      const responseText = document.getElementById('responseText');

      if (!question) {
        alert('Please enter a question');
        return;
      }

      responseBox.classList.remove('show', 'error');
      loading.classList.add('show');
      submitBtn.disabled = true;
      buttonText.textContent = 'Processing...';

      try {
        const response = await fetch(`${API_URL}/generate`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ question })
        });

        const data = await response.json();

        loading.classList.remove('show');
        submitBtn.disabled = false;
        buttonText.textContent = 'Ask Question';
        responseBox.classList.add('show');

        if (response.ok) {
          responseText.textContent = data.response;
        } else {
          responseBox.classList.add('error');
          responseText.textContent = data.detail || 'An error occurred';
        }
      } catch (error) {
        loading.classList.remove('show');
        submitBtn.disabled = false;
        buttonText.textContent = 'Ask Question';
        responseBox.classList.add('show', 'error');
        responseText.textContent = `Error: ${error.message}. Make sure the server is running!`;
      }
    });

    // Ctrl+Enter shortcut
    document.getElementById('question').addEventListener('keydown', (e) => {
      if (e.ctrlKey && e.key === 'Enter') {
        e.preventDefault();
        document.getElementById('qaForm').dispatchEvent(new Event('submit'));
      }
    });
  </script>
</body>
</html>

#main.py
import requests
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import os
from dotenv import load_dotenv
import json
from datetime import datetime
from pathlib import Path

# Load environment variables
load_dotenv()

app = FastAPI()

# Allow frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

HISTORY_FILE = "qa-history.json"

class Prompt(BaseModel):
    question: str = Field(..., min_length=1, description="Question cannot be empty")

def load_history():
    if Path(HISTORY_FILE).exists():
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_to_history(question, answer):
    history = load_history()
    history.append({
        "timestamp": datetime.now().isoformat(),
        "question": question,
        "answer": answer
    })
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=2, ensure_ascii=False)

@app.post("/generate")
async def generate_response(prompt: Prompt):
    if not prompt.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    try:
        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key:
            raise HTTPException(status_code=500, detail="Missing OpenRouter API key")

        # Debug log to confirm key is loaded
        print("Using OpenRouter API key:", api_key[:10] + "...")

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        body = {
            "model": "mistralai/mistral-7b-instruct:free",  # free Mistral model
            "messages": [
                {"role": "user", "content": f"Question: {prompt.question}\n\nAnswer:"}
            ],
            "max_tokens": 500,
            "temperature": 0.7
        }

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=body
        )

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)

        data = response.json()
        answer = data["choices"][0]["message"]["content"]

        save_to_history(prompt.question, answer)

        return {"question": prompt.question, "response": answer}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.get("/history")
async def get_history():
    return load_history()

# qa-history.json

[
  {
    "timestamp": "2025-11-07T15:00:05.123456",
    "question": "What is the capital of India?",
    "answer": "The capital of India is New Delhi."
  },
  {
    "timestamp": "2025-11-07T15:07:12.654321",
    "question": "Name a programming language used for web development.",
    "answer": "JavaScript is widely used for web development."
  },
  {
    "timestamp": "2025-11-07T15:13:45.987654",
    "question": "What is the largest planet in our solar system?",
    "answer": "Jupiter is the largest planet in our solar system."
  },
  {
    "timestamp": "2025-11-07T15:19:30.246810",
    "question": "Who wrote 'Romeo and Juliet'?",
    "answer": "William Shakespeare wrote 'Romeo and Juliet'."
  },
  {
    "timestamp": "2025-11-07T15:21:01.753130",
    "question": "What causes lightning?",
    "answer": "Lightning is caused by the buildup and discharge of electrical energy in the atmosphere, primarily within thunderstorms. It involves charge separation in clouds, the strengthening of the electric field, and the eventual discharge of energy through ionized air channels, producing a bright flash and thunder."
  },
  {
    "timestamp": "2025-11-07T15:26:00.112233",
    "question": "Explain FastAPI in simple terms.",
    "answer": "FastAPI is a modern Python framework for building APIs quickly. It uses type hints, generates documentation automatically, and is very fast because it’s built on Starlette and Pydantic."
  }
]
