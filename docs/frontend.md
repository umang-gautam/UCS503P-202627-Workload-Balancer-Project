# Frontend

React 19, Vite 6, Tailwind 3, react-router 7. Lives in `code/frontend`.

## Pages

The look follows the institute's LMS (Moodle, Moove theme): white top bar with
the TIET logo, a left navigation drawer, maroon primary actions, bordered white
cards and tables on a light-gray page. Poppins for type. No decoration.

| Route | File | What it does |
|---|---|---|
| `/` | `pages/Dashboard.jsx` | Summary tiles and the priority queue for the selected student |
| `/students` | `pages/Students.jsx` | Add and delete students, manage which subjects each is enrolled in |
| `/subjects` | `pages/Subjects.jsx` | Subjects, their topics, and the deadlines under each topic |
| `/scores` | `pages/PerformanceEntry.jsx` | Log a score per topic, browse the score history |
| `/study-plan` | `pages/StudyPlanView.jsx` | Generate a plan, sessions grouped by day, mark done/missed, run the agent |

The student is chosen once, in the top bar. `context/StudentContext.jsx` holds
the list and the selection and every page reads it with `useStudents()`.

## Shared pieces

- `components/ui.jsx`: the kit every page composes: `PageHeader`, `Card`, `Button`, `Input`, `Select`, `Field`, `Table`, `Badge`, `ProgressBar`, `Alert`, `EmptyState`, `Spinner`, plus `bandFor(priority)` for the red/amber/green thresholds at 70 and 30.
- `components/Layout.jsx`: top bar with logo and student switcher, left drawer (bottom tab bar on phones), content area.
- `components/TopicRow.jsx`: one scored topic as a table row with priority, mastery and urgency bars.
- `components/ScoreBadge.jsx`: a score pill. Green at 80+, amber at 50+, red below.
- `components/SessionBlock.jsx`: one study session as a table row with a pending / done / missed control.
- `hooks/useStudyPlan.js`: plans, selected plan, sessions and the optimistic status update for a student.
- `api/client.js`: the only place `fetch` is called. One function per endpoint. Non-JSON responses (proxy error pages, text 500s) become readable error messages instead of a `JSON.parse` crash.
- `lib/selectedStudent.js`: the selected student is remembered in `localStorage`, so switching pages or reloading keeps it.

## Talking to the backend

Every request goes to `/api/...`.

- `npm run dev`: Vite proxies `/api` to `http://127.0.0.1:8000`.
- Docker: nginx proxies `/api/` to the `backend` service.
- Hosted separately: set `VITE_API_BASE` at build time (see `.env.example`).

The client never needs to know which of the three it is running under.

## Conventions

- Pages own their own data with `useState` and `useEffect`. The only shared state is the selected student, provided by `StudentContext`.
- Every async action has its own loading and error state, keyed by id when the action is per-row. A failed request shows the backend's message verbatim next to the thing that failed.
- Status changes are optimistic and revert on failure.
- An empty database shows a **Load demo data** button on the Dashboard, which calls `POST /api/demo/seed`.
- Styling is Tailwind utility classes through the kit in `components/ui.jsx`. Colours are semantic tokens (`surface`, `edge`, `fg`, `brand`) backed by CSS variables in `index.css`; pages never use raw gray or white classes.
- Light and dark themes are a variable swap under a `dark` class on `<html>`. The toggle in the top bar remembers the choice; with no choice saved the OS preference wins. `?theme=dark` in the URL forces it, which is how screenshots are taken.

## Commands

```sh
npm install
npm run dev        # http://localhost:5173
npm run build      # dist/
npm run preview    # serve dist/ locally
```
