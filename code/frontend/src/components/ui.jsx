/**
 * Small UI kit. Every page composes these instead of styling by hand,
 * so the app has one look: bordered white cards on a light-gray page,
 * maroon primary actions, tables for lists.
 */

const TONES = {
  red:   { badge: 'bg-red-50 text-red-700 ring-red-200',         bar: 'bg-red-600' },
  amber: { badge: 'bg-amber-50 text-amber-800 ring-amber-200',   bar: 'bg-amber-500' },
  green: { badge: 'bg-green-50 text-green-700 ring-green-200',   bar: 'bg-green-600' },
  blue:  { badge: 'bg-sky-50 text-sky-800 ring-sky-200',         bar: 'bg-steel-600' },
  gray:  { badge: 'bg-gray-100 text-gray-700 ring-gray-200',     bar: 'bg-gray-400' },
  brand: { badge: 'bg-brand-50 text-brand-700 ring-brand-100',   bar: 'bg-brand-700' },
};

/** Priority band, same thresholds the scoring engine documents. */
export function bandFor(priority) {
  const p = Number(priority) || 0;
  if (p > 70) return { label: 'Urgent', tone: 'red' };
  if (p >= 30) return { label: 'Moderate', tone: 'amber' };
  return { label: 'On track', tone: 'green' };
}

export function PageHeader({ title, subtitle, actions }) {
  return (
    <div className="mb-5 flex flex-wrap items-end justify-between gap-3 border-b border-gray-200 pb-4">
      <div>
        <h1 className="text-2xl font-semibold text-gray-900">{title}</h1>
        {subtitle && <p className="mt-1 text-sm text-gray-500">{subtitle}</p>}
      </div>
      {actions && <div className="flex items-center gap-2">{actions}</div>}
    </div>
  );
}

export function Card({ title, actions, children, className = '', padded = true }) {
  return (
    <section className={`rounded border border-gray-200 bg-white ${className}`}>
      {(title || actions) && (
        <header className="flex items-center justify-between gap-3 border-b border-gray-200 px-4 py-3">
          <h2 className="text-sm font-semibold uppercase tracking-wide text-gray-700">{title}</h2>
          {actions}
        </header>
      )}
      <div className={padded ? 'p-4' : ''}>{children}</div>
    </section>
  );
}

const BUTTON = {
  primary: 'bg-brand-700 text-white hover:bg-brand-800 focus:ring-brand-600',
  secondary: 'border border-gray-300 bg-white text-gray-800 hover:bg-gray-50 focus:ring-gray-400',
  danger: 'border border-red-200 bg-white text-red-700 hover:bg-red-50 focus:ring-red-400',
  ghost: 'text-brand-700 hover:bg-brand-50 focus:ring-brand-600',
};

export function Button({ variant = 'primary', size = 'md', className = '', ...props }) {
  const sz = size === 'sm' ? 'px-2.5 py-1 text-xs' : 'px-3.5 py-2 text-sm';
  return (
    <button
      type="button"
      className={`inline-flex items-center justify-center gap-1.5 rounded font-medium transition focus:outline-none focus:ring-2 focus:ring-offset-1 disabled:cursor-not-allowed disabled:opacity-50 ${sz} ${BUTTON[variant]} ${className}`}
      {...props}
    />
  );
}

const CONTROL =
  'block w-full rounded border border-gray-300 bg-white px-3 py-2 text-sm text-gray-900 shadow-sm focus:border-brand-600 focus:outline-none focus:ring-1 focus:ring-brand-600 disabled:bg-gray-50';

export function Input({ className = '', ...props }) {
  return <input className={`${CONTROL} ${className}`} {...props} />;
}

export function Select({ className = '', children, ...props }) {
  return <select className={`${CONTROL} ${className}`} {...props}>{children}</select>;
}

export function Field({ label, htmlFor, hint, children, className = '' }) {
  return (
    <div className={className}>
      <label htmlFor={htmlFor} className="mb-1 block text-xs font-medium uppercase tracking-wide text-gray-600">
        {label}
      </label>
      {children}
      {hint && <p className="mt-1 text-xs text-gray-500">{hint}</p>}
    </div>
  );
}

const ALERT = {
  error: 'border-red-200 bg-red-50 text-red-800',
  success: 'border-green-200 bg-green-50 text-green-800',
  info: 'border-sky-200 bg-sky-50 text-sky-900',
};

export function Alert({ kind = 'info', children, onRetry, className = '' }) {
  return (
    <div role={kind === 'error' ? 'alert' : 'status'} className={`flex items-start justify-between gap-3 rounded border px-3 py-2 text-sm ${ALERT[kind]} ${className}`}>
      <div className="whitespace-pre-line">{children}</div>
      {onRetry && (
        <button type="button" onClick={onRetry} className="text-xs font-semibold underline">
          Retry
        </button>
      )}
    </div>
  );
}

export function EmptyState({ title, children, action }) {
  return (
    <div className="rounded border border-dashed border-gray-300 bg-white px-6 py-10 text-center">
      <h3 className="text-base font-semibold text-gray-900">{title}</h3>
      {children && <p className="mx-auto mt-1 max-w-md text-sm text-gray-500">{children}</p>}
      {action && <div className="mt-4">{action}</div>}
    </div>
  );
}

export function Spinner({ label = 'Loading…' }) {
  return (
    <div className="flex items-center gap-2 px-1 py-2 text-sm text-gray-500">
      <span className="h-4 w-4 animate-spin rounded-full border-2 border-gray-300 border-t-brand-700" />
      {label}
    </div>
  );
}

export function Badge({ tone = 'gray', children, className = '' }) {
  return (
    <span className={`inline-flex items-center rounded px-2 py-0.5 text-xs font-medium ring-1 ring-inset ${TONES[tone].badge} ${className}`}>
      {children}
    </span>
  );
}

export function ProgressBar({ value, tone = 'brand', className = '' }) {
  const v = Math.min(Math.max(Number(value) || 0, 0), 100);
  return (
    <div className={`h-1.5 w-full overflow-hidden rounded bg-gray-100 ${className}`}>
      <div className={`h-full ${TONES[tone].bar}`} style={{ width: `${v}%` }} />
    </div>
  );
}

/** Table with a header row. `head` is an array of labels; children are <tr>s. */
export function Table({ head, children, className = '' }) {
  return (
    <div className={`overflow-x-auto ${className}`}>
      <table className="min-w-full divide-y divide-gray-200 text-sm">
        <thead className="bg-gray-50">
          <tr>
            {head.map((h, i) => (
              <th key={i} scope="col" className="px-4 py-2 text-left text-xs font-semibold uppercase tracking-wide text-gray-600">
                {h}
              </th>
            ))}
          </tr>
        </thead>
        <tbody className="divide-y divide-gray-100 bg-white">{children}</tbody>
      </table>
    </div>
  );
}

export const td = 'px-4 py-2.5 align-middle';

export function formatDate(iso) {
  if (!iso) return '';
  const d = new Date(iso);
  return isNaN(d) ? iso : d.toLocaleDateString(undefined, { day: 'numeric', month: 'short', year: 'numeric' });
}
