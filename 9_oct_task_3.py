#task - create a middleware that calculates how long each request
# takes to execute and returns it in the response header

from fastapi import FastAPI, Request
import time
import asyncio

app = FastAPI()

# Middleware to measure request duration and add it to response headers
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = (time.time() - start_time) * 1000  # milliseconds
    response.headers["X-Process-Time-ms"] = f"{process_time:.2f}"
    return response

# Example route
@app.get("/users")
async def get_users():
    await asyncio.sleep(0.2)  # simulate processing delay

    return {"users": ["Dhruv", "Damon"]}