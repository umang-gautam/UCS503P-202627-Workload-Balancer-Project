"""
Curriculum catalog repository.

Supports multiple branches. Currently populated with B.E. (Computer Engineering - COE)
and designed for seamless addition of other branches (ECE, ENC, ME, etc.).
"""

from app.data.branches.coe import COE_COURSES, COE_PROGRAM_INFO, COE_STUDENTS

# Registry of available academic branches
BRANCH_REGISTRY = {
    "COE": {
        "info": COE_PROGRAM_INFO,
        "students": COE_STUDENTS,
        "courses": COE_COURSES,
    },
}


def get_available_branches() -> list[str]:
    """Return list of registered branch codes."""
    return list(BRANCH_REGISTRY.keys())


def get_branch_data(branch_code: str = "COE") -> dict:
    """Retrieve syllabus and student data for a specific branch."""
    branch = branch_code.upper()
    if branch not in BRANCH_REGISTRY:
        raise ValueError(f"Branch '{branch}' not found. Available: {get_available_branches()}")
    return BRANCH_REGISTRY[branch]


def get_all_courses(branch_code: str | None = None) -> list[dict]:
    """Retrieve courses for a specific branch, or all branches if None."""
    if branch_code:
        return get_branch_data(branch_code)["courses"]
    courses = []
    for branch_data in BRANCH_REGISTRY.values():
        courses.extend(branch_data["courses"])
    return courses


def get_all_students(branch_code: str | None = None) -> list[dict]:
    """Retrieve students for a specific branch, or all branches if None."""
    if branch_code:
        return get_branch_data(branch_code)["students"]
    students = []
    for branch_data in BRANCH_REGISTRY.values():
        students.extend(branch_data["students"])
    return students
