import { Routes, Route, NavLink, Link } from 'react-router-dom'
import Dashboard from './pages/Dashboard'
import Subjects from './pages/Subjects'
import PerformanceEntry from './pages/PerformanceEntry'
import StudyPlanView from './pages/StudyPlanView'

const NAV = [
  { to: '/', label: 'Dashboard', end: true },
  { to: '/subjects', label: 'Subjects' },
  { to: '/performance', label: 'Scores' },
  { to: '/study-plan', label: 'Study Plan' },
]

/**
 * App shell — sticky navigation bar + page routing.
 * The selected student is remembered across pages (see lib/selectedStudent.js).
 */
export default function App() {
  return (
    <div className="min-h-screen flex flex-col bg-gray-50">
      <nav className="sticky top-0 z-20 bg-indigo-600 text-white shadow-lg">
        <div className="max-w-6xl mx-auto px-4 py-3 flex items-center gap-6">
          <Link to="/" className="flex items-center gap-2 text-xl font-bold tracking-tight">
            <span className="inline-flex w-8 h-8 rounded-lg bg-white/15 items-center justify-center text-base">⚖️</span>
            Workload Balancer
          </Link>
          <div className="flex gap-1 text-sm font-medium">
            {NAV.map(({ to, label, end }) => (
              <NavLink
                key={to}
                to={to}
                end={end}
                className={({ isActive }) =>
                  `px-3 py-1.5 rounded-lg transition ${
                    isActive ? 'bg-white/20 text-white' : 'text-indigo-100 hover:bg-white/10 hover:text-white'
                  }`
                }
              >
                {label}
              </NavLink>
            ))}
          </div>
        </div>
      </nav>

      <main className="flex-1 w-full max-w-6xl mx-auto px-4 py-6">
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/subjects" element={<Subjects />} />
          <Route path="/performance" element={<PerformanceEntry />} />
          <Route path="/study-plan" element={<StudyPlanView />} />
        </Routes>
      </main>

      <footer className="border-t border-gray-200 py-4 text-center text-xs text-gray-500">
        AI-Powered Student Workload Balancer · UCS503P, TIET Patiala ·{' '}
        <a href="/api/docs" className="underline hover:text-gray-700">API docs</a>
      </footer>
    </div>
  )
}
