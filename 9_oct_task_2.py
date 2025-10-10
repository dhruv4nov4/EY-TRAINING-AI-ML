from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import logging
import time
import traceback

app = FastAPI()

# ---------------- SETUP STRUCTURED LOGGING ----------------
logging.basicConfig(
    filename="app.log",
    format="%(asctime)s | %(levelname)s | %(message)s",
    level=logging.INFO
)

# setting visit count as 0 - global visit counter
visit_count = 0

# ---------------- REQUEST LOGGING MIDDLEWARE + VISIT COUNTER ----------------
@app.middleware("http")
async def visit_counter_middleware(request: Request, call_next):
    global visit_count
    start = time.time()

    # Increment visit count on every request
    visit_count += 1
    logging.info(f"Visit #{visit_count} | Path: {request.url.path}")

    try:
        response = await call_next(request)
    except Exception as e:
        duration = round(time.time() - start, 3)
        logging.error(
            f"Exception in {request.method} {request.url.path}: {str(e)}\n{traceback.format_exc()}"
        )
        raise e

    # Add timing and visit info to logs and response
    duration = round(time.time() - start, 3)
    logging.info(
        f"{request.method} {request.url.path} | Status: {response.status_code} | Duration: {duration}s"
    )
    response.headers["X-Total-Visits"] = str(visit_count)
    return response

# ---------------- ROUTES(to see the visit counter running)----------------
@app.get("/")
def home():
    return {
        "message": "Welcome to the Site!!!",
        "total_visits": visit_count,
        "info": "Refresh the page to see the number increase."
    }

@app.get("/visits")
def get_visits():
    #---Get the current total visit count---
    return {"total_visits": visit_count}

# ---------------- GLOBAL EXCEPTION HANDLER ----------------
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logging.error(
        f"Unhandled error in {request.url.path}: {str(exc)}\n{traceback.format_exc()}"
    )
    return JSONResponse(
        status_code=500,
        content={"error": "Internal Server Error", "detail": str(exc)},
    )