# backend/main.py
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from datetime import datetime
import time
import logging

# -----------------------------------------------------------------------------
# App & Middleware
# -----------------------------------------------------------------------------
app = FastAPI(title="Streamlit + FastAPI Demo", version="1.0.0")

# CORS (allow all for local dev; tighten in prod)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Basic logger
logger = logging.getLogger("api")
logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")

# Simple logging middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.perf_counter()
    response = None
    try:
        response = await call_next(request)
        return response
    finally:
        duration_ms = (time.perf_counter() - start) * 1000
        logger.info(
            "%s %s -> %s (%.2f ms)",
            request.method,
            request.url.path,
            getattr(response, "status_code", "ERR"),
            duration_ms,
        )

# -----------------------------------------------------------------------------
# Schemas
# -----------------------------------------------------------------------------
class TextInput(BaseModel):
    text: str = Field(..., min_length=1, description="Any non-empty string")

class ModelRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Text to analyze")

class AddResponse(BaseModel):
    result: int

class DateResponse(BaseModel):
    date: str

class ReverseResponse(BaseModel):
    reversed: str

class ModelResponse(BaseModel):
    label: str
    score: float

# -----------------------------------------------------------------------------
# Health
# -----------------------------------------------------------------------------
@app.get("/health")
def health():
    return {"status": "ok"}

# -----------------------------------------------------------------------------
# Endpoints required by your spec
# -----------------------------------------------------------------------------
@app.get("/add", response_model=AddResponse)
def add_numbers(a: int, b: int):
    """Add two integers given as query params."""
    return AddResponse(result=a + b)

@app.get("/date", response_model=DateResponse)
def get_date():
    """Return today's date in YYYY-MM-DD."""
    return DateResponse(date=datetime.now().strftime("%Y-%m-%d"))

@app.post("/reverse", response_model=ReverseResponse)
def reverse_word(payload: TextInput):
    """Reverse the input text."""
    return ReverseResponse(reversed=payload.text[::-1])

# -----------------------------------------------------------------------------
# POST — FastAPI — Model in it (toy sentiment model)
# -----------------------------------------------------------------------------
POSITIVE_WORDS = {"good", "great", "awesome", "love", "excellent", "nice", "happy"}
NEGATIVE_WORDS = {"bad", "terrible", "hate", "awful", "poor", "sad", "worse"}

def simple_sentiment(text: str) -> ModelResponse:
    """
    A tiny rule-based model:
    score = (#positive - #negative) / max(1, total_matches)
    label = positive/negative/neutral based on score
    """
    tokens = [t.strip(".,!?;:").lower() for t in text.split()]
    pos = sum(1 for t in tokens if t in POSITIVE_WORDS)
    neg = sum(1 for t in tokens if t in NEGATIVE_WORDS)
    total = max(1, pos + neg)
    score = (pos - neg) / total

    if score > 0.2:
        label = "positive"
    elif score < -0.2:
        label = "negative"
    else:
        label = "neutral"
    return ModelResponse(label=label, score=round(score, 3))

@app.post("/model/predict", response_model=ModelResponse)
def model_predict(payload: ModelRequest):
    """
    Accepts text and returns a label + score from the toy sentiment model.
    """
    try:
        return simple_sentiment(payload.text)
    except Exception as e:
        # Example of explicit error surfacing
        raise HTTPException(status_code=400, detail=f"Model error: {e}")

# -----------------------------------------------------------------------------
# Error example (optional)
# -----------------------------------------------------------------------------
@app.get("/boom")
def boom():
    raise HTTPException(status_code=418, detail="I'm a teapot ☕")