"""
Demo seed: a small, realistic dataset so the app has something to show.

Goes through the entity services like any other caller. Idempotent: if the
demo students already exist, nothing is written.
"""

from datetime import date, timedelta

from app.services import (
    assignment_service,
    enrollment_service,
    performance_service,
    student_service,
    subject_service,
    topic_service,
)

DEMO_STUDENTS = [
    {"name": "Asha Verma", "email": "asha.demo@workload.local"},
    {"name": "Rohan Mehta", "email": "rohan.demo@workload.local"},
]

# subject -> topics -> (assignment due in N days, scores for Asha, scores for Rohan)
DEMO_CURRICULUM = {
    ("UCS503", "Software Engineering"): {
        "Requirements & Use Cases": (3, [82, 88], [55]),
        "UML & Design Patterns": (10, [64], [40, 48]),
        "Testing Strategies": (21, [], [70]),
    },
    ("UCS301", "Data Structures"): {
        "Linked Lists": (5, [45, 52], [90, 94]),
        "Trees & Graphs": (2, [38], [61]),
        "Hashing": (30, [75, 80], []),
    },
    ("UMA101", "Linear Algebra"): {
        "Eigenvalues": (7, [58], [72, 68]),
        "Matrix Decomposition": (14, [], [35]),
    },
}


async def seed(today: date | None = None) -> dict:
    today = today or date.today()
    existing = await student_service.get_students()
    if any(s["email"] == DEMO_STUDENTS[0]["email"] for s in existing):
        return {"seeded": False, "message": "Demo data already present."}

    students = [await student_service.create_student(s) for s in DEMO_STUDENTS]
    counts = {"students": len(students), "subjects": 0, "topics": 0,
              "enrollments": 0, "assignments": 0, "performance_records": 0}

    for (code, name), topics in DEMO_CURRICULUM.items():
        subject = await subject_service.create_subject({"code": code, "name": name})
        counts["subjects"] += 1
        for student in students:
            await enrollment_service.create_enrollment(
                {"student_id": student["id"], "subject_id": subject["id"]})
            counts["enrollments"] += 1
        for topic_name, (due_in, asha_scores, rohan_scores) in topics.items():
            topic = await topic_service.create_topic({"subject_id": subject["id"], "name": topic_name})
            counts["topics"] += 1
            await assignment_service.create_assignment({
                "topic_id": topic["id"],
                "title": f"{topic_name} assignment",
                "due_date": (today + timedelta(days=due_in)).isoformat(),
            })
            counts["assignments"] += 1
            for student, scores in zip(students, (asha_scores, rohan_scores)):
                for score in scores:
                    await performance_service.create_performance_record(
                        {"student_id": student["id"], "topic_id": topic["id"], "score": score})
                    counts["performance_records"] += 1

    return {"seeded": True, "message": "Demo data created.", **counts}
