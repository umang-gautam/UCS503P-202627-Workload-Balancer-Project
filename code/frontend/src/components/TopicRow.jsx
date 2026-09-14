import { Badge, ProgressBar, bandFor, td } from './ui.jsx';

/** One scored topic as a table row: rank, topic, subject, priority, mastery, urgency. */
export default function TopicRow({ topic, rank }) {
  const priority = Number(topic.priority) || 0;
  const mastery = Math.round((Number(topic.mastery) || 0) * 100);
  const urgency = Math.round((Number(topic.urgency) || 0) * 100);
  const band = bandFor(priority);
  return (
    <tr>
      <td className={`${td} w-12 text-fg-subtle`}>{rank}</td>
      <td className={td}>
        <div className="font-medium text-fg">{topic.topic_name}</div>
        <div className="text-xs text-fg-subtle">{topic.subject_name}</div>
      </td>
      <td className={`${td} w-48`}>
        <div className="mb-1 flex items-center justify-between text-xs">
          <Badge tone={band.tone}>{band.label}</Badge>
          <span className="font-semibold text-fg">{priority.toFixed(1)}</span>
        </div>
        <ProgressBar value={priority} tone={band.tone} />
      </td>
      <td className={`${td} w-36`}>
        <div className="mb-1 text-xs text-fg-muted">{mastery}%</div>
        <ProgressBar value={mastery} tone="blue" />
      </td>
      <td className={`${td} w-36`}>
        <div className="mb-1 text-xs text-fg-muted">{urgency}%</div>
        <ProgressBar value={urgency} tone="amber" />
      </td>
    </tr>
  );
}
