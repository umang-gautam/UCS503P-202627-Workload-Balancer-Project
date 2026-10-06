# Setup

Everything lives under `code/`. No accounts are needed: docker compose brings
up a local Postgres with PostgREST in front of it, which speaks the same REST
API as Supabase.

## Run everything with Docker

```sh
cd code
docker compose up --build
```

- App: <http://localhost:8080>
- API through the frontend proxy: <http://localhost:8080/api/health>, Swagger at `/api/docs`
- PostgREST directly: <http://localhost:3000>

If `postgrest` exits on first start, an older `pgdata` volume is in the way: `docker compose down -v` and start again.

With `AUTO_SEED=true` (the default in compose and `.env.example`), the backend automatically seeds the authentic TIET college dataset on startup whenever the database is empty. You can also re-seed or trigger it manually from the Dashboard, via CLI (`python seed.py` or `python seed.py --reset`), or via curl:

```sh
curl -X POST localhost:8080/api/demo/seed
```

That creates four TIET students (Umang, Vriti, Khushi, Shaurya), five core curriculum subjects (UCS503 Software Engineering, UCS301 DSA, UCS303 OS, UCS505 Computer Networks, UCS310 DBMS), seventeen topics with upcoming deadlines, and realistic student performance scores. It is fully idempotent. The endpoint exists only when `DEBUG=true`, which compose sets.

## Using a real Supabase project instead

Paste `code/backend/schema.sql` into the project's SQL editor once, then either
export these before `docker compose up`, or put them in `code/backend/.env` for a
bare uvicorn:

```sh
SUPABASE_URL=https://<project-ref>.supabase.co
SUPABASE_REST_PATH=/rest/v1
SUPABASE_KEY=<service-role or secret key>
```

`.env` is git-ignored and docker-ignored. Keep it that way.

## Run the pieces directly

Backend, Python 3.10+. Keep `docker compose up db postgrest` running for the
data, and copy `.env.example` to `.env` (its defaults point at that PostgREST):

```sh
cd code/backend
cp .env.example .env
python -m venv venv && source venv/bin/activate     # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload                        # http://localhost:8000/docs
```

Frontend, Node 22:

```sh
cd code/frontend
npm install
npm run dev                                          # http://localhost:5173, proxies /api to :8000
```

## Tests

From the repository root:

```sh
pytest
```

No credentials or network needed. Route tests patch services, agent tests patch
the agent's tools, and the scoring and allocation tests are pure functions.

## Adding an entity

Follow `students` through the layers: schema in `app/schemas/`, repository in
`app/repositories/`, service in `app/services/`, router in `app/api/routes/`,
then `include_router` in `app/main.py`. Add the table to `schema.sql` and the
client functions to `frontend/src/api/client.js`.
