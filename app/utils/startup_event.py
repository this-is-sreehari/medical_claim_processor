from app.db.database import engine
from app.models.claim_model import Base
from sqlalchemy.exc import OperationalError
from main import app
import asyncio


@app.on_event("startup")
async def startup_event():
    retries = 10
    for attempt in range(retries):
        try:
            async with engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)
            print("Connected to DB and created tables.")
            return
        except OperationalError:
            print(f"DB not ready yet... retrying {attempt+1}/{retries}")
            await asyncio.sleep(3)
