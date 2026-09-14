import { NavLink } from 'react-router-dom';
import { useStudents } from '../context/StudentContext.jsx';
import { Select } from './ui.jsx';

const NAV = [
  { to: '/', label: 'Dashboard', end: true, icon: 'M3 12l9-8 9 8v8a1 1 0 01-1 1h-5v-6H9v6H4a1 1 0 01-1-1z' },
  { to: '/students', label: 'Students', icon: 'M16 11a4 4 0 10-8 0 4 4 0 008 0zm-9 9a5 5 0 0110 0H7z' },
  { to: '/subjects', label: 'Subjects', icon: 'M4 5a2 2 0 012-2h12a2 2 0 012 2v14a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm4 2v10h8V7H8z' },
  { to: '/scores', label: 'Scores', icon: 'M4 19h16M6 17V9m4 8V5m4 12v-6m4 6V7' },
  { to: '/study-plan', label: 'Study plan', icon: 'M7 3v2m10-2v2M4 8h16M5 5h14a1 1 0 011 1v13a1 1 0 01-1 1H5a1 1 0 01-1-1V6a1 1 0 011-1z' },
];

function Icon({ d }) {
  return (
    <svg className="h-4 w-4 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
      <path d={d} />
    </svg>
  );
}

function StudentSwitcher() {
  const { students, selectedId, setSelectedId, loading, error } = useStudents();
  if (error) return <span className="text-xs text-red-200">{error}</span>;
  return (
    <label className="flex items-center gap-2 text-xs font-medium text-gray-600">
      <span className="hidden sm:inline">Student</span>
      <Select
        value={selectedId}
        onChange={(e) => setSelectedId(e.target.value)}
        disabled={loading || students.length === 0}
        className="!w-56 !py-1.5"
        aria-label="Selected student"
      >
        {students.length === 0 && <option value="">{loading ? 'Loading…' : 'No students yet'}</option>}
        {students.map((s) => (
          <option key={s.id} value={s.id}>{s.name}</option>
        ))}
      </Select>
    </label>
  );
}

/** Moodle-style shell: white top bar with the institute logo, left drawer, gray content area. */
export default function Layout({ children }) {
  return (
    <div className="min-h-screen">
      <header className="sticky top-0 z-20 border-b border-gray-200 bg-white">
        <div className="flex h-14 items-center justify-between gap-4 px-4">
          <NavLink to="/" className="flex items-center gap-3">
            <img src="/tiet-logo.svg" alt="TIET" className="h-8 w-8" />
            <span className="leading-tight">
              <span className="block text-base font-semibold text-brand-700">Workload Balancer</span>
              <span className="block text-[11px] uppercase tracking-wide text-gray-500">Thapar Institute · UCS503P</span>
            </span>
          </NavLink>
          <StudentSwitcher />
        </div>
      </header>

      <div className="flex">
        <aside className="sticky top-14 hidden h-[calc(100vh-3.5rem)] w-56 shrink-0 border-r border-gray-200 bg-white md:block">
          <nav className="py-3" aria-label="Main">
            {NAV.map(({ to, label, end, icon }) => (
              <NavLink
                key={to}
                to={to}
                end={end}
                className={({ isActive }) =>
                  `flex items-center gap-3 border-l-4 px-4 py-2.5 text-sm ${
                    isActive
                      ? 'border-brand-700 bg-brand-50 font-medium text-brand-700'
                      : 'border-transparent text-gray-700 hover:bg-gray-50'
                  }`
                }
              >
                <Icon d={icon} />
                {label}
              </NavLink>
            ))}
          </nav>
          <div className="absolute inset-x-0 bottom-0 border-t border-gray-200 px-4 py-3 text-[11px] text-gray-500">
            <a href="/api/docs" className="hover:text-brand-700">API documentation</a>
          </div>
        </aside>

        <nav className="fixed inset-x-0 bottom-0 z-20 flex border-t border-gray-200 bg-white md:hidden" aria-label="Main">
          {NAV.map(({ to, label, end }) => (
            <NavLink key={to} to={to} end={end} className={({ isActive }) => `flex-1 py-2 text-center text-[11px] ${isActive ? 'font-semibold text-brand-700' : 'text-gray-600'}`}>
              {label}
            </NavLink>
          ))}
        </nav>

        <main className="min-w-0 flex-1 px-4 pb-20 pt-6 sm:px-6 md:pb-8">
          <div className="mx-auto max-w-6xl">{children}</div>
        </main>
      </div>
    </div>
  );
}
