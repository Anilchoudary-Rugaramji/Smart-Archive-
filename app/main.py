from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)


@app.get("/")
def root():
    return {"message": f"{settings.PROJECT_NAME} backend is running"}
