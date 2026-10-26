"""Notification routes: email a student their study reminders."""
from fastapi import APIRouter, HTTPException

from app.schemas.notification import ReminderResult
from app.services import notification_service

router = APIRouter()


@router.post("/reminders/{student_id}", response_model=ReminderResult)
async def send_reminders(student_id: str):
    """Email the student their upcoming study sessions and deadlines."""
    result = await notification_service.send_study_reminders(student_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return result
