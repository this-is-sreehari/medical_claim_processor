from fastapi import FastAPI
from app.db.database import engine
from app.models.claim_model import Base


app = FastAPI()

@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
async def root():
    return {"message": "Hello, World!"}
