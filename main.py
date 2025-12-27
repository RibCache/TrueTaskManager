from fastapi import FastAPI
from src.routers.crud import router as tasks

app = FastAPI()

app.include_router(tasks)
