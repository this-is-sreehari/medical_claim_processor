from fastapi import APIRouter, UploadFile, File, Depends
from app.services.orchestrator import Orchestrator
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db_session
from app.models.claim_model import Claim
from sqlalchemy import select


router = APIRouter()
orch = Orchestrator()

@router.post("/process-claim")
async def process_claim(
    files: list[UploadFile] = File(...),
    db: AsyncSession = Depends(get_db_session)
):
    claim_result = await orch.process(files)

    status = claim_result["claim_decision"]["status"]

    claim = Claim(
        status=status,
        data=claim_result
    )

    db.add(claim)
    await db.commit()
    await db.refresh(claim)

    return {
        "db_record": {
            "id": claim.id,
            "status": claim.status
        },
        "claim_data": claim.data
    }

@router.get("/claims")
async def get_all_claims(db: AsyncSession = Depends(get_db_session)):
    stmt = select(Claim)
    result = await db.execute(stmt)
    claims = result.scalars().all()

    return [
        {
            "id": claim.id,
            "status": claim.status,
            "data": claim.data
        }
        for claim in claims
    ]
