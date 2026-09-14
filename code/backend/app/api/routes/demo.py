"""Demo data endpoint. Only available when DEBUG=true."""

from fastapi import APIRouter, HTTPException, status

from app.core.config import settings
from app.services import demo_service

router = APIRouter()


@router.post("/seed", status_code=status.HTTP_201_CREATED)
async def seed_demo_data():
    """Create two students, three subjects with topics, deadlines and scores."""
    if not settings.debug:
        raise HTTPException(status_code=403, detail="Demo seeding is disabled unless DEBUG=true")
    return await demo_service.seed()
