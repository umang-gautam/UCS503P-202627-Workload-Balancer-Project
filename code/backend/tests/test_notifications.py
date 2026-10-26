from unittest.mock import AsyncMock, patch

from app.services.notification_service import build_reminder_email

STUDENT = {"id": "s1", "name": "Asha", "email": "asha@example.com"}
SESSIONS = [{"date": "2026-11-01", "topic_name": "Trees", "duration_minutes": 45, "status": "pending"}]
DEADLINES = [{"due_date": "2026-11-03", "title": "Trees assignment", "topic_name": "Trees"}]


def test_build_reminder_email_includes_items():
    subject, body = build_reminder_email(STUDENT, SESSIONS, DEADLINES)
    assert "1 session(s), 1 deadline(s)" in subject
    assert "Asha" in body and "Trees" in body and "2026-11-03" in body


def test_build_reminder_email_empty():
    subject, body = build_reminder_email(STUDENT, [], [])
    assert "0 session(s), 0 deadline(s)" in subject
    assert "No pending study sessions" in body


def test_reminders_route_404_for_unknown_student(client):
    with patch("app.api.routes.notifications.notification_service") as svc:
        svc.send_study_reminders = AsyncMock(return_value=None)
        assert client.post("/notifications/reminders/nope").status_code == 404


def test_reminders_route_ok(client):
    with patch("app.api.routes.notifications.notification_service") as svc:
        svc.send_study_reminders = AsyncMock(return_value={
            "student_id": "s1", "email": "asha@example.com",
            "sessions": 2, "deadlines": 1, "sent": True, "reason": None,
        })
        r = client.post("/notifications/reminders/s1")
    assert r.status_code == 200 and r.json()["sessions"] == 2 and r.json()["sent"] is True
