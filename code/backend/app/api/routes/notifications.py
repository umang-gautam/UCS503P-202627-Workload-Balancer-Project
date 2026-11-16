"""Notification routes: compose a student's study reminders for delivery."""
from fastapi import APIRouter, HTTPException

from app.schemas.notification import ReminderResult
from app.services import notification_service

router = APIRouter()


@router.post("/reminders/{student_id}", response_model=ReminderResult)
async def send_reminders(student_id: str):
    """Compose the student's upcoming study-session and deadline reminder.

    Returns the subject + message; the frontend delivers it via Web3Forms.
    """
    result = await notification_service.compose_student_reminder(student_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return result
