import { td } from './ui.jsx';

const STATUS = {
  pending: { label: 'Pending', tone: 'blue' },
  done: { label: 'Done', tone: 'green' },
  missed: { label: 'Missed', tone: 'red' },
};

/** One study session as a table row; the segmented control shows and sets its status. */
export default function SessionBlock({ session, topicName, isUpdating, onStatusChange }) {
  return (
    <tr className={isUpdating ? 'opacity-60' : ''}>
      <td className={td}>
        <div className="font-medium text-fg">{topicName}</div>
      </td>
      <td className={`${td} w-28 text-fg-muted`}>{session.duration_minutes} min</td>
      <td className={`${td} w-56`}>
        <div className="inline-flex overflow-hidden rounded border border-edge-strong">
          {Object.entries(STATUS).map(([key, { label }]) => {
            const active = session.status === key;
            return (
              <button
                key={key}
                type="button"
                disabled={isUpdating || active}
                onClick={() => onStatusChange(session.id, key)}
                className={`px-2.5 py-1 text-xs ${active ? 'bg-brand-700 font-medium text-white' : 'bg-surface text-fg-muted hover:bg-surface-2'} disabled:cursor-default`}
              >
                {label}
              </button>
            );
          })}
        </div>
      </td>
    </tr>
  );
}
