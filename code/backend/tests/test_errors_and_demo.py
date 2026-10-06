from unittest.mock import AsyncMock, patch
import pytest

import httpx

from app.core.config import settings
from app.data.curriculum_catalog import get_available_branches
from app.services import demo_service
from app.main import auto_seed_if_needed


def test_unreachable_database_is_a_json_503(client):
    req = httpx.Request("GET", "http://db.invalid/rest/v1/students")
    with patch("app.api.routes.students.student_service") as svc:
        svc.get_students = AsyncMock(side_effect=httpx.ConnectError("boom", request=req))
        resp = client.get("/students/")
    assert resp.status_code == 503
    assert resp.headers["content-type"].startswith("application/json")
    assert "db.invalid" in resp.json()["message"]


def test_demo_seed_disabled_without_debug(client, monkeypatch):
    monkeypatch.setattr(settings, "debug", False)
    assert client.post("/demo/seed").status_code == 403


def test_list_available_branches(client):
    resp = client.get("/demo/branches")
    assert resp.status_code == 200
    assert "COE" in resp.json()["branches"]


def test_demo_seed_runs_when_debug(client, monkeypatch):
    monkeypatch.setattr(settings, "debug", True)
    with patch("app.api.routes.demo.demo_service") as svc:
        svc.seed = AsyncMock(return_value={"seeded": True, "students": 4, "branch": "COE"})
        resp = client.post("/demo/seed")
    assert resp.status_code == 201
    assert resp.json()["students"] == 4
    svc.seed.assert_awaited_once_with(reset=False, branch_code="COE")


def test_demo_seed_with_reset_flag(client, monkeypatch):
    monkeypatch.setattr(settings, "debug", True)
    with patch("app.api.routes.demo.demo_service") as svc:
        svc.seed = AsyncMock(return_value={"seeded": True, "students": 4, "branch": "COE"})
        resp = client.post("/demo/seed?reset=true&branch=COE")
    assert resp.status_code == 201
    svc.seed.assert_awaited_once_with(reset=True, branch_code="COE")


def test_demo_seed_invalid_branch(client, monkeypatch):
    monkeypatch.setattr(settings, "debug", True)
    resp = client.post("/demo/seed?branch=NONEXISTENT")
    assert resp.status_code == 400
    assert "not found" in resp.json()["detail"]


@pytest.mark.asyncio
async def test_demo_service_seed_idempotent_when_already_seeded():
    with patch("app.services.student_service.get_students") as mock_get:
        mock_get.return_value = [{"email": "ugautam_be24@thapar.edu", "id": "s-1"}]
        result = await demo_service.seed()
        assert result["seeded"] is False
        assert "already present" in result["message"]


@pytest.mark.asyncio
async def test_demo_service_seed_creates_curriculum():
    with patch("app.services.student_service.get_students", AsyncMock(return_value=[])), \
         patch("app.services.student_service.create_student", AsyncMock(side_effect=lambda s: {"id": f"s-{s['email']}", **s})), \
         patch("app.services.subject_service.get_subjects", AsyncMock(return_value=[])), \
         patch("app.services.subject_service.create_subject", AsyncMock(side_effect=lambda s: {"id": f"sub-{s['code']}", **s})), \
         patch("app.services.enrollment_service.get_enrollments_by_student", AsyncMock(return_value=[])), \
         patch("app.services.enrollment_service.create_enrollment", AsyncMock(return_value={"id": "e-1"})), \
         patch("app.services.topic_service.get_topics_by_subject", AsyncMock(return_value=[])), \
         patch("app.services.topic_service.create_topic", AsyncMock(side_effect=lambda t: {"id": f"t-{t['name']}", **t})), \
         patch("app.services.assignment_service.create_assignment", AsyncMock(return_value={"id": "a-1"})), \
         patch("app.services.performance_service.create_performance_record", AsyncMock(return_value={"id": "p-1"})):
        result = await demo_service.seed(branch_code="COE")
        assert result["seeded"] is True
        assert result["students"] == 4
        assert result["subjects"] > 0
        assert result["enrollments"] > 0
        assert result["assignments"] > 0
        assert result["performance_records"] > 0


@pytest.mark.asyncio
async def test_auto_seed_skips_when_invalid_domain(monkeypatch):
    monkeypatch.setattr(settings, "supabase_url", "http://supabase.invalid")
    monkeypatch.setattr(settings, "auto_seed", True)
    with patch("app.services.student_service.get_students") as mock_get:
        await auto_seed_if_needed()
        mock_get.assert_not_called()


@pytest.mark.asyncio
async def test_auto_seed_runs_when_database_empty(monkeypatch):
    monkeypatch.setattr(settings, "supabase_url", "http://localhost:3000")
    monkeypatch.setattr(settings, "auto_seed", True)
    with patch("app.services.student_service.get_students", AsyncMock(return_value=[])), \
         patch("app.services.demo_service.seed", AsyncMock(return_value={"seeded": True})) as mock_seed:
        await auto_seed_if_needed()
        mock_seed.assert_awaited_once()
