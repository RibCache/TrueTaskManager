from fastapi import FastAPI
from src.routers.crud import router as tasks
from src.routers.auth import router as auth
import redis.asyncio as redis

app = FastAPI()

app.include_router(tasks)
app.include_router(auth)

redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)

@app.get("/counter")
async def get_counter():
    count = await redis_client.incr("visits_count")
    
    return {
        "message": "Hello",
        "total_visits": count
    }
