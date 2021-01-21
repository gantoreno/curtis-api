from fastapi import FastAPI
from .router import diagnosis_router

app = FastAPI()

app.include_router(diagnosis_router.router)
