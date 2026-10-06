"""
College demo seed: authentic TIET curriculum and student dataset.

Supports multiple branches via app.data.curriculum_catalog.
Currently seeds B.E. (COE - Computer Engineering) with official syllabus units,
assignments, deadlines, and multi-tier student performance evaluations.

Goes through the entity services like any other caller. Fully idempotent.
"""

import asyncio
from datetime import date, timedelta
import logging

from app.data.curriculum_catalog import (
    BRANCH_REGISTRY,
    get_all_courses,
    get_all_students,
    get_available_branches,
    get_branch_data,
)
from app.services import (
    assignment_service,
    enrollment_service,
    performance_service,
    student_service,
    subject_service,
    topic_service,
)

logger = logging.getLogger("app.services.demo_service")

# Backwards compatibility exports
DEMO_STUDENTS = get_all_students("COE")
COLLEGE_STUDENTS = DEMO_STUDENTS


async def seed(
    today: date | None = None,
    reset: bool = False,
    branch_code: str = "COE",
) -> dict:
    """
    Seed authentic TIET college students, subjects, topics, assignments and performance scores.

    If reset=True, existing college students and their related records are cleared first.
    Otherwise, if college data already exists, the function safely returns early.
    """
    today = today or date.today()
    branch_data = get_branch_data(branch_code)
    branch_students = branch_data["students"]
    branch_courses = branch_data["courses"]

    existing_students = await student_service.get_students()
    existing_emails = {s["email"]: s for s in existing_students}
    target_emails = {s["email"] for s in branch_students}

    if reset:
        logger.info("Resetting existing students for branch %s...", branch_code)
        for s in existing_students:
            if s["email"] in target_emails:
                await student_service.delete_student(s["id"])
        existing_students = await student_service.get_students()
        existing_emails = {s["email"]: s for s in existing_students}
    elif any(email in existing_emails for email in target_emails):
        return {
            "seeded": False,
            "message": f"Real college data for {branch_code} already present.",
            "branch": branch_code,
        }

    # 1. Create or load students
    students_by_email = {}
    students_created = 0
    for s_data in branch_students:
        email = s_data["email"]
        if email in existing_emails:
            students_by_email[email] = existing_emails[email]
        else:
            created = await student_service.create_student({
                "name": s_data["name"],
                "email": email,
            })
            students_by_email[email] = created
            students_created += 1

    counts = {
        "branch": branch_code,
        "students": len(branch_students),
        "students_created": students_created,
        "subjects": 0,
        "topics": 0,
        "enrollments": 0,
        "assignments": 0,
        "performance_records": 0,
    }

    # 2. Cache existing subjects
    existing_subjects = await subject_service.get_subjects()
    subject_by_code = {s["code"]: s for s in existing_subjects}

    # 3. Create subjects & topics from the branch curriculum
    for course in branch_courses:
        code = course["code"]
        name = course["name"]

        if code in subject_by_code:
            subject = subject_by_code[code]
        else:
            subject = await subject_service.create_subject({"code": code, "name": name})
            subject_by_code[code] = subject
            counts["subjects"] += 1

        # Enroll all students in this subject if not already enrolled
        for student in students_by_email.values():
            existing_enrollments = await enrollment_service.get_enrollments_by_student(student["id"])
            enrolled_subject_ids = {e["subject_id"] for e in existing_enrollments}
            if subject["id"] not in enrolled_subject_ids:
                await enrollment_service.create_enrollment({
                    "student_id": student["id"],
                    "subject_id": subject["id"],
                })
                counts["enrollments"] += 1

        # Cache existing topics for this subject
        existing_topics = await topic_service.get_topics_by_subject(subject["id"])
        topic_by_name = {t["name"]: t for t in existing_topics}

        for topic_info in course.get("topics", []):
            topic_name = topic_info["name"]
            if topic_name in topic_by_name:
                topic = topic_by_name[topic_name]
            else:
                topic = await topic_service.create_topic({
                    "subject_id": subject["id"],
                    "name": topic_name,
                })
                topic_by_name[topic_name] = topic
                counts["topics"] += 1

            due_days = topic_info.get("due_days", 14)
            assignment_title = topic_info.get("assignment", f"{topic_name} assignment")
            await assignment_service.create_assignment({
                "topic_id": topic["id"],
                "title": assignment_title,
                "due_date": (today + timedelta(days=due_days)).isoformat(),
            })
            counts["assignments"] += 1

            scores_map = topic_info.get("scores", {})
            for email, scores in scores_map.items():
                student = students_by_email.get(email)
                if not student:
                    continue
                for score in scores:
                    await performance_service.create_performance_record({
                        "student_id": student["id"],
                        "topic_id": topic["id"],
                        "score": score,
                    })
                    counts["performance_records"] += 1

    return {
        "seeded": True,
        "message": f"Real TIET {branch_code} college data created.",
        **counts,
    }


if __name__ == "__main__":
    result = asyncio.run(seed())
    print("Seed result:", result)
