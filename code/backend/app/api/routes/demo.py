"""Demo data endpoint. Only available when DEBUG=true."""

from fastapi import APIRouter, HTTPException, Query, status

from app.core.config import settings
from app.data.curriculum_catalog import get_available_branches
from app.services import demo_service

router = APIRouter()


@router.get("/branches")
async def list_available_branches():
    """List academic branches available for seeding."""
    return {"branches": get_available_branches()}


@router.post("/seed", status_code=status.HTTP_201_CREATED)
async def seed_demo_data(
    reset: bool = Query(False, description="Reset and re-seed college data"),
    branch: str = Query("COE", description="Branch code to seed (e.g. COE)"),
):
    """Create real TIET college students, subjects with topics, deadlines and scores."""
    if not settings.debug:
        raise HTTPException(status_code=403, detail="Demo seeding is disabled unless DEBUG=true")
    try:
        return await demo_service.seed(reset=reset, branch_code=branch)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
