import os
from dotenv import load_dotenv
from fastapi import FastAPI
# Load environment variables
load_dotenv()

app = FastAPI()

APP_NAME = os.getenv("APP_NAME", "Default App")
APP_ENV = os.getenv("APP_ENV", "production")
SECRET_KEY = os.getenv("SECRET_KEY", "no-secret")


@app.get("/")
def home():
    return {
        "message": f"Welcome to {APP_NAME}",
        "environment": APP_ENV
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.get("/secret")
def secret():
    return {
        "secret_key": SECRET_KEY
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )