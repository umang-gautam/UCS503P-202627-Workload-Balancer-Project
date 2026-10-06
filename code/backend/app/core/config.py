"""
Application configuration via pydantic-settings.

Reads from a .env file (or real environment variables in production).
Every setting is declared once here with its type — if a required value
is missing, the app will refuse to start with a clear error message.
"""

from pathlib import Path
from pydantic_settings import BaseSettings

_BACKEND_DIR = Path(__file__).resolve().parent.parent.parent
_ENV_FILE = _BACKEND_DIR / ".env"


class Settings(BaseSettings):
    """All environment-driven configuration for the backend."""

    # ── Data store ────────────────────────────────────────────
    # Supabase:        SUPABASE_URL=https://<ref>.supabase.co  SUPABASE_KEY=<key>
    # Local PostgREST: SUPABASE_URL=http://localhost:3000      SUPABASE_REST_PATH=  (empty)
    supabase_url: str
    supabase_key: str = ""            # empty = no auth headers (local PostgREST anon)
    supabase_rest_path: str = "/rest/v1"

    # ── Application ───────────────────────────────────────────
    app_name: str = "Workload Balancer API"
    debug: bool = False               # also enables POST /demo/seed
    auto_seed: bool = True            # auto-populate college data on startup if database is empty

    # ── CORS ──────────────────────────────────────────────────
    cors_origins: str = "http://localhost:5173"

    model_config = {
        "env_file": (_ENV_FILE if _ENV_FILE.exists() else ".env"),
        "env_file_encoding": "utf-8",
        "extra": "ignore",
    }

    @property
    def cors_origin_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",")]

    @property
    def rest_base_url(self) -> str:
        return self.supabase_url.rstrip("/") + self.supabase_rest_path


settings = Settings()
