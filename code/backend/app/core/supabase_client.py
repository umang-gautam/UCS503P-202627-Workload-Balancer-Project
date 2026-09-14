"""
Async HTTP client for a PostgREST API: Supabase in production, a local
PostgREST container in docker compose.

Every repository uses this client. It handles the base URL, the auth
headers (only when a key is configured) and "Prefer: return=representation"
so INSERT/UPDATE/DELETE responses include the affected rows.
No business logic lives here.
"""

import httpx

from app.core.config import settings

_HEADERS = {
    "Content-Type": "application/json",
    "Prefer": "return=representation",
}
if settings.supabase_key:
    _HEADERS["apikey"] = settings.supabase_key
    _HEADERS["Authorization"] = f"Bearer {settings.supabase_key}"


def get_client() -> httpx.AsyncClient:
    """A fresh short-lived client per call; avoids event-loop lifetime issues."""
    return httpx.AsyncClient(base_url=settings.rest_base_url, headers=_HEADERS, timeout=15.0)
