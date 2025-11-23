from fastapi import APIRouter, UploadFile, File, Depends, status, HTTPException
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
    try:
        claim_result = await orch.process(files)

        claim_status = claim_result.get("claim_decision", {}).get("status", "")
        if claim_status:
            claim = Claim(
                status=claim_status,
                data=claim_result
            )

            db.add(claim)
            await db.commit()
            await db.refresh(claim)

            return {
                "data": claim.data
            }
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Unexpected error: {str(e)}"
        )

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
