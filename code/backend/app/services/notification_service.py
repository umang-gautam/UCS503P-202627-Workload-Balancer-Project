"""
Email notifications: study-session reminders and upcoming deadline alerts.

Provider-agnostic SMTP driven by settings (SMTP_HOST/PORT/USER/PASS/FROM/TLS).
When SMTP_HOST is empty, sending is a no-op so the app still runs with no mail
server. `build_reminder_email` is a pure function (no I/O) and is unit-tested.
"""
from datetime import date, timedelta
from email.message import EmailMessage

import aiosmtplib

from app.core.config import settings
from app.repositories import (
    assignment_repo,
    enrollment_repo,
    student_repo,
    study_plan_repo,
    study_session_repo,
    topic_repo,
)


def _as_date(value):
    """Coerce an ISO string or date to a date, or None if it cannot."""
    if isinstance(value, date):
        return value
    try:
        return date.fromisoformat(str(value))
    except (TypeError, ValueError):
        return None


def build_reminder_email(student: dict, sessions: list[dict], deadlines: list[dict]) -> tuple[str, str]:
    """Pure: compose (subject, body) from a student and their upcoming items."""
    name = student.get("name") or "there"
    horizon = settings.reminder_horizon_days
    lines = [
        f"Hi {name},",
        "",
        f"Here is your study reminder for the next {horizon} days.",
        "",
    ]
    if sessions:
        lines.append("Upcoming study sessions:")
        for s in sessions:
            topic = s.get("topic_name") or s.get("topic_id")
            lines.append(f"  - {s['date']}: {topic} for {s['duration_minutes']} min")
        lines.append("")
    else:
        lines.append("No pending study sessions in this window.")
        lines.append("")
    if deadlines:
        lines.append("Upcoming deadlines:")
        for d in deadlines:
            topic = d.get("topic_name") or ""
            lines.append(f"  - {d['due_date']}: {d['title']} ({topic})")
        lines.append("")
    lines += ["Keep it up!", "— Workload Balancer"]
    subject = f"Study reminder: {len(sessions)} session(s), {len(deadlines)} deadline(s)"
    return subject, "\n".join(lines)


async def _send_email(to_addr: str, subject: str, body: str) -> dict:
    if not settings.email_enabled:
        return {"sent": False, "reason": "SMTP not configured"}
    msg = EmailMessage()
    msg["From"] = settings.smtp_from
    msg["To"] = to_addr
    msg["Subject"] = subject
    msg.set_content(body)
    await aiosmtplib.send(
        msg,
        hostname=settings.smtp_host,
        port=settings.smtp_port,
        username=settings.smtp_user or None,
        password=settings.smtp_pass or None,
        start_tls=settings.smtp_tls,
    )
    return {"sent": True, "reason": None}


async def _gather_upcoming(student_id: str, today: date, horizon: int) -> tuple[list[dict], list[dict]]:
    cutoff = today + timedelta(days=horizon)

    # Pending sessions from the student's most recent plan, within the window.
    sessions: list[dict] = []
    plans = await study_plan_repo.get_by_student(student_id)
    topic_names: dict[str, str] = {}
    if plans:
        plan = sorted(plans, key=lambda p: str(p.get("start_date", "")), reverse=True)[0]
        for s in await study_session_repo.get_by_plan(plan["id"]):
            sd = _as_date(s.get("date"))
            if s.get("status") == "pending" and (sd is None or today <= sd <= cutoff):
                sessions.append(s)

    # Deadlines within the window for the student's enrolled topics.
    deadlines: list[dict] = []
    for enrollment in await enrollment_repo.get_by_student(student_id):
        for topic in await topic_repo.get_by_subject(enrollment["subject_id"]):
            topic_names[topic["id"]] = topic["name"]
            for assignment in await assignment_repo.get_by_topic(topic["id"]):
                dd = _as_date(assignment.get("due_date"))
                if dd is None or today <= dd <= cutoff:
                    deadlines.append({**assignment, "topic_name": topic["name"]})

    for s in sessions:
        s["topic_name"] = topic_names.get(s["topic_id"], s["topic_id"])
    sessions.sort(key=lambda s: str(s["date"]))
    deadlines.sort(key=lambda d: str(d["due_date"]))
    return sessions, deadlines


async def send_study_reminders(student_id: str, horizon: int | None = None) -> dict | None:
    """Orchestrate: gather the student's upcoming items and email them.

    Returns None if the student does not exist.
    """
    horizon = horizon or settings.reminder_horizon_days
    today = date.today()
    student = await student_repo.get_by_id(student_id)
    if not student:
        return None
    sessions, deadlines = await _gather_upcoming(student_id, today, horizon)
    subject, body = build_reminder_email(student, sessions, deadlines)
    result = await _send_email(student["email"], subject, body)
    return {
        "student_id": student_id,
        "email": student["email"],
        "sessions": len(sessions),
        "deadlines": len(deadlines),
        **result,
    }
