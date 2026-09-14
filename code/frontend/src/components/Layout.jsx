import { useState } from 'react';
import { NavLink } from 'react-router-dom';
import { applyTheme, getTheme } from '../lib/theme.js';
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
    <label className="flex items-center gap-2 text-xs font-medium text-fg-muted">
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

function ThemeToggle() {
  const [theme, setTheme] = useState(getTheme);
  const next = theme === 'dark' ? 'light' : 'dark';
  const flip = () => { applyTheme(next); setTheme(next); };
  return (
    <button
      type="button"
      onClick={flip}
      aria-label={`Switch to ${next} theme`}
      title={`Switch to ${next} theme`}
      className="rounded border border-edge-strong p-1.5 text-fg-muted hover:bg-surface-2"
    >
      {theme === 'dark' ? (
        <svg className="h-4 w-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4" /><path d="M12 2v2m0 16v2M2 12h2m16 0h2M4.9 4.9l1.4 1.4m11.4 11.4l1.4 1.4M4.9 19.1l1.4-1.4m11.4-11.4l1.4-1.4" /></svg>
      ) : (
        <svg className="h-4 w-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1111.2 3a7 7 0 009.8 9.8z" /></svg>
      )}
    </button>
  );
}

/** Moodle-style shell: white top bar with the institute logo, left drawer, gray content area. */
export default function Layout({ children }) {
  return (
    <div className="min-h-screen">
      <header className="sticky top-0 z-20 border-b border-edge bg-surface">
        <div className="flex h-14 items-center justify-between gap-4 px-4">
          <NavLink to="/" className="flex items-center gap-3">
            <img src="/tiet-logo.svg" alt="TIET" className="h-8 w-8" />
            <span className="leading-tight">
              <span className="block text-base font-semibold text-brand-700">Workload Balancer</span>
              <span className="block text-[11px] uppercase tracking-wide text-fg-subtle">Thapar Institute · UCS503P</span>
            </span>
          </NavLink>
          <div className="flex items-center gap-3">
            <StudentSwitcher />
            <ThemeToggle />
          </div>
        </div>
      </header>

      <div className="flex">
        <aside className="sticky top-14 hidden h-[calc(100vh-3.5rem)] w-56 shrink-0 border-r border-edge bg-surface md:block">
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
                      : 'border-transparent text-fg-muted hover:bg-surface-2'
                  }`
                }
              >
                <Icon d={icon} />
                {label}
              </NavLink>
            ))}
          </nav>
          <div className="absolute inset-x-0 bottom-0 border-t border-edge px-4 py-3 text-[11px] text-fg-subtle">
            <a href="/api/docs" className="hover:text-brand-700">API documentation</a>
          </div>
        </aside>

        <nav className="fixed inset-x-0 bottom-0 z-20 flex border-t border-edge bg-surface md:hidden" aria-label="Main">
          {NAV.map(({ to, label, end }) => (
            <NavLink key={to} to={to} end={end} className={({ isActive }) => `flex-1 py-2 text-center text-[11px] ${isActive ? 'font-semibold text-brand-700' : 'text-fg-muted'}`}>
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
