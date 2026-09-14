import { Badge } from './ui.jsx';

/** Score pill: green at 80+, amber at 50+, red below. */
export default function ScoreBadge({ score }) {
  const s = Number(score) || 0;
  const tone = s >= 80 ? 'green' : s >= 50 ? 'amber' : 'red';
  return <Badge tone={tone}>{s}%</Badge>;
}
