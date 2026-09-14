from unittest.mock import AsyncMock, patch

import httpx

from app.core.config import settings


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


def test_demo_seed_runs_when_debug(client, monkeypatch):
    monkeypatch.setattr(settings, "debug", True)
    with patch("app.api.routes.demo.demo_service") as svc:
        svc.seed = AsyncMock(return_value={"seeded": True, "students": 2})
        resp = client.post("/demo/seed")
    assert resp.status_code == 201
    assert resp.json()["students"] == 2
