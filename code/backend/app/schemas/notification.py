"""Schema for the notification/reminder endpoints."""
from pydantic import BaseModel


class ReminderResult(BaseModel):
    student_id: str
    email: str
    sessions: int
    deadlines: int
    sent: bool
    reason: str | None = None
