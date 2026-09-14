/**
 * Small UI kit. Every page composes these instead of styling by hand,
 * so the app has one look: bordered white cards on a light-gray page,
 * maroon primary actions, tables for lists.
 */

const TONES = {
  red:   { badge: 'bg-red-50 text-red-700 ring-red-200 dark:bg-red-950/60 dark:text-red-300 dark:ring-red-900',           bar: 'bg-red-600' },
  amber: { badge: 'bg-amber-50 text-amber-800 ring-amber-200 dark:bg-amber-950/60 dark:text-amber-300 dark:ring-amber-900', bar: 'bg-amber-500' },
  green: { badge: 'bg-green-50 text-green-700 ring-green-200 dark:bg-green-950/60 dark:text-green-300 dark:ring-green-900', bar: 'bg-green-600' },
  blue:  { badge: 'bg-sky-50 text-sky-800 ring-sky-200 dark:bg-sky-950/60 dark:text-sky-300 dark:ring-sky-900',             bar: 'bg-steel-600 dark:bg-sky-500' },
  gray:  { badge: 'bg-surface-3 text-fg-muted ring-edge',                                                                    bar: 'bg-gray-400' },
  brand: { badge: 'bg-brand-50 text-brand-700 ring-brand-100',                                                               bar: 'bg-brand-700' },
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
    <div className="mb-5 flex flex-wrap items-end justify-between gap-3 border-b border-edge pb-4">
      <div>
        <h1 className="text-2xl font-semibold text-fg">{title}</h1>
        {subtitle && <p className="mt-1 text-sm text-fg-subtle">{subtitle}</p>}
      </div>
      {actions && <div className="flex items-center gap-2">{actions}</div>}
    </div>
  );
}

export function Card({ title, actions, children, className = '', padded = true }) {
  return (
    <section className={`rounded border border-edge bg-surface ${className}`}>
      {(title || actions) && (
        <header className="flex items-center justify-between gap-3 border-b border-edge px-4 py-3">
          <h2 className="text-sm font-semibold uppercase tracking-wide text-fg-muted">{title}</h2>
          {actions}
        </header>
      )}
      <div className={padded ? 'p-4' : ''}>{children}</div>
    </section>
  );
}

const BUTTON = {
  primary: 'bg-brand-700 text-white hover:bg-brand-800 focus:ring-brand-600',
  secondary: 'border border-edge-strong bg-surface text-fg hover:bg-surface-2 focus:ring-gray-400',
  danger: 'border border-red-200 bg-surface text-red-700 hover:bg-red-50 focus:ring-red-400 dark:border-red-900 dark:text-red-300 dark:hover:bg-red-950/50',
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
  'block w-full rounded border border-edge-strong bg-surface px-3 py-2 text-sm text-fg placeholder:text-fg-subtle shadow-sm focus:border-brand-600 focus:outline-none focus:ring-1 focus:ring-brand-600 disabled:bg-surface-2';

export function Input({ className = '', ...props }) {
  return <input className={`${CONTROL} ${className}`} {...props} />;
}

export function Select({ className = '', children, ...props }) {
  return <select className={`${CONTROL} ${className}`} {...props}>{children}</select>;
}

export function Field({ label, htmlFor, hint, children, className = '' }) {
  return (
    <div className={className}>
      <label htmlFor={htmlFor} className="mb-1 block text-xs font-medium uppercase tracking-wide text-fg-muted">
        {label}
      </label>
      {children}
      {hint && <p className="mt-1 text-xs text-fg-subtle">{hint}</p>}
    </div>
  );
}

const ALERT = {
  error: 'border-red-200 bg-red-50 text-red-800 dark:border-red-900 dark:bg-red-950/50 dark:text-red-200',
  success: 'border-green-200 bg-green-50 text-green-800 dark:border-green-900 dark:bg-green-950/50 dark:text-green-200',
  info: 'border-sky-200 bg-sky-50 text-sky-900 dark:border-sky-900 dark:bg-sky-950/50 dark:text-sky-200',
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
    <div className="rounded border border-dashed border-edge-strong bg-surface px-6 py-10 text-center">
      <h3 className="text-base font-semibold text-fg">{title}</h3>
      {children && <p className="mx-auto mt-1 max-w-md text-sm text-fg-subtle">{children}</p>}
      {action && <div className="mt-4">{action}</div>}
    </div>
  );
}

export function Spinner({ label = 'Loading…' }) {
  return (
    <div className="flex items-center gap-2 px-1 py-2 text-sm text-fg-subtle">
      <span className="h-4 w-4 animate-spin rounded-full border-2 border-edge-strong border-t-brand-700" />
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
    <div className={`h-1.5 w-full overflow-hidden rounded bg-surface-3 ${className}`}>
      <div className={`h-full ${TONES[tone].bar}`} style={{ width: `${v}%` }} />
    </div>
  );
}

/** Table with a header row. `head` is an array of labels; children are <tr>s. */
export function Table({ head, children, className = '' }) {
  return (
    <div className={`overflow-x-auto ${className}`}>
      <table className="min-w-full divide-y divide-edge text-sm">
        <thead className="bg-surface-2">
          <tr>
            {head.map((h, i) => (
              <th key={i} scope="col" className="px-4 py-2 text-left text-xs font-semibold uppercase tracking-wide text-fg-muted">
                {h}
              </th>
            ))}
          </tr>
        </thead>
        <tbody className="divide-y divide-edge bg-surface">{children}</tbody>
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
