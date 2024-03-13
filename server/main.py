import uvicorn
from fastapi import FastAPI

from src.api.api import api_router

app = FastAPI()
app.include_router(
    api_router,
    prefix="/api",
    tags=["api"],
)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8080,
    )
