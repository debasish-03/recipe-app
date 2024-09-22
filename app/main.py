from fastapi import FastAPI, APIRouter, HTTPException, Request, Depends
from typing import Optional, Any
from app.schemas.recipe import RecipeSearchResults, Recipe, RecipeCreate

from pathlib import Path
from app.api.api_v1.api import api_router
from app.core.config import settings

# Project Directories
ROOT = Path(__file__).resolve().parent.parent
BASE_PATH = Path(__file__).resolve().parent

root_router = APIRouter()
app = FastAPI(title="Recipe API")

@root_router.get("/", status_code=200)
def root() -> dict:
    """
    Root Get
    """
    return {"msg": "Hello, World!"}

app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(root_router)

if __name__ == "__main__":
    #  netstat -ano | grep :8001
    # Win + R => cmd => taskkill /PID 1552 /F
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")