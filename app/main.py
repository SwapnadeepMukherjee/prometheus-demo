import asyncio
import random
from fastapi import FastAPI, Response
# from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import      Instrumentator

app = FastAPI(title="Async FastAPI with Prometheus")

# This one line handles the /metrics endpoint and default histograms:
Instrumentator().instrument(app).expose(app)

@app.get("/")
async def root():
    return {"message": "FASTAPI with Prometheus is running"}

# Simulate an async operation:
@app.get("/heavy")
async def heavy():
    # Simulate a heavy async latency operation:
    wait_time = random.uniform(0.1, 0.8)
    await asyncio.sleep(wait_time)
    return {"status": "slow", "waited": wait_time}

@app.get("/error")
async def error(response: Response):
    #Simulate a random failure:
    response.status_code = 500
    return {"error": "Simulated Internal Server Error"}