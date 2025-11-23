from fastapi import FastAPI
from app.routes.process_claim import router

app = FastAPI()

app.include_router(router)

from app.utils import startup_event
