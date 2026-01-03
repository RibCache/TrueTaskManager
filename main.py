from fastapi import FastAPI
from src.routers.crud import router as tasks
from src.routers.auth import router as auth

app = FastAPI()

app.include_router(tasks)
app.include_router(auth)

