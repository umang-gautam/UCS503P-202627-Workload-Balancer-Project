import { Badge, ProgressBar, bandFor, td } from './ui.jsx';

/** One scored topic as a table row: rank, topic, subject, priority, mastery, urgency. */
export default function TopicRow({ topic, rank }) {
  const priority = Number(topic.priority) || 0;
  const mastery = Math.round((Number(topic.mastery) || 0) * 100);
  const urgency = Math.round((Number(topic.urgency) || 0) * 100);
  const band = bandFor(priority);
  return (
    <tr>
      <td className={`${td} w-12 text-gray-500`}>{rank}</td>
      <td className={td}>
        <div className="font-medium text-gray-900">{topic.topic_name}</div>
        <div className="text-xs text-gray-500">{topic.subject_name}</div>
      </td>
      <td className={`${td} w-48`}>
        <div className="mb-1 flex items-center justify-between text-xs">
          <Badge tone={band.tone}>{band.label}</Badge>
          <span className="font-semibold text-gray-900">{priority.toFixed(1)}</span>
        </div>
        <ProgressBar value={priority} tone={band.tone} />
      </td>
      <td className={`${td} w-36`}>
        <div className="mb-1 text-xs text-gray-700">{mastery}%</div>
        <ProgressBar value={mastery} tone="blue" />
      </td>
      <td className={`${td} w-36`}>
        <div className="mb-1 text-xs text-gray-700">{urgency}%</div>
        <ProgressBar value={urgency} tone="amber" />
      </td>
    </tr>
  );
}
