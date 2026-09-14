import { useEffect, useState } from 'react';
import { createPerformanceRecord, fetchPerformanceByStudent, fetchStudentScores } from '../api/client.js';
import { useStudents } from '../context/StudentContext.jsx';
import ScoreBadge from '../components/ScoreBadge.jsx';
import { Alert, Badge, Button, Card, EmptyState, Input, PageHeader, Spinner, Table, bandFor, td } from '../components/ui.jsx';

export default function PerformanceEntry() {
  const { selected, selectedId, students, loading: loadingStudents } = useStudents();
  const [topics, setTopics] = useState([]);
  const [records, setRecords] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [inputs, setInputs] = useState({});
  const [saving, setSaving] = useState(null);
  const [notice, setNotice] = useState(null);

  const load = async (id) => {
    if (!id) { setTopics([]); setRecords([]); return; }
    setLoading(true);
    setError(null);
    try {
      const [t, r] = await Promise.all([fetchStudentScores(id), fetchPerformanceByStudent(id)]);
      setTopics(t || []);
      setRecords(r || []);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };
  useEffect(() => { setInputs({}); setNotice(null); load(selectedId); }, [selectedId]);

  const save = async (topic) => {
    const value = Number(inputs[topic.topic_id]);
    if (!Number.isFinite(value) || value < 0 || value > 100) {
      setNotice({ kind: 'error', text: 'Score must be a number from 0 to 100.' });
      return;
    }
    setSaving(topic.topic_id);
    setNotice(null);
    try {
      await createPerformanceRecord({ student_id: selectedId, topic_id: topic.topic_id, score: value });
      setInputs({ ...inputs, [topic.topic_id]: '' });
      setNotice({ kind: 'success', text: `Saved ${value}% for ${topic.topic_name}.` });
      await load(selectedId);
    } catch (err) {
      setNotice({ kind: 'error', text: err.message });
    } finally {
      setSaving(null);
    }
  };

  const topicName = (id) => topics.find((t) => t.topic_id === id)?.topic_name || id;
  const history = [...records].sort((a, b) => (b.recorded_at || '').localeCompare(a.recorded_at || ''));

  let body;
  if (loadingStudents || loading) body = <Spinner />;
  else if (!selectedId) body = <EmptyState title="No student selected">{students.length ? 'Pick a student in the top bar.' : 'Add a student first.'}</EmptyState>;
  else if (error) body = <Alert kind="error" onRetry={() => load(selectedId)}>{error}</Alert>;
  else if (topics.length === 0) body = <EmptyState title="No enrolled topics">{selected?.name} has no subjects with topics yet.</EmptyState>;
  else body = (
    <div className="space-y-4">
      {notice && <Alert kind={notice.kind}>{notice.text}</Alert>}
      <Card title="Log a score" padded={false}>
        <Table head={['Topic', 'Mastery', 'Priority', 'New score (0–100)', '']}>
          {topics.map((t) => {
            const band = bandFor(t.priority);
            return (
              <tr key={t.topic_id}>
                <td className={td}>
                  <div className="font-medium text-fg">{t.topic_name}</div>
                  <div className="text-xs text-fg-subtle">{t.subject_name}</div>
                </td>
                <td className={`${td} w-28 text-fg-muted`}>{Math.round(t.mastery * 100)}%</td>
                <td className={`${td} w-36`}><Badge tone={band.tone}>{band.label} · {t.priority.toFixed(0)}</Badge></td>
                <td className={`${td} w-44`}>
                  <Input
                    type="number" min="0" max="100" step="1" placeholder="0–100"
                    value={inputs[t.topic_id] ?? ''}
                    onChange={(e) => setInputs({ ...inputs, [t.topic_id]: e.target.value })}
                    onKeyDown={(e) => e.key === 'Enter' && save(t)}
                    className="!py-1.5"
                  />
                </td>
                <td className={`${td} w-24 text-right`}>
                  <Button size="sm" disabled={saving === t.topic_id || inputs[t.topic_id] === undefined || inputs[t.topic_id] === ''} onClick={() => save(t)}>
                    {saving === t.topic_id ? 'Saving…' : 'Save'}
                  </Button>
                </td>
              </tr>
            );
          })}
        </Table>
      </Card>

      <Card title={`History · ${history.length} record${history.length === 1 ? '' : 's'}`} padded={false}>
        {history.length === 0 ? <p className="px-4 py-3 text-sm text-fg-subtle">No scores logged yet.</p> : (
          <Table head={['Recorded', 'Topic', 'Score']}>
            {history.map((r) => (
              <tr key={r.id}>
                <td className={`${td} w-52 whitespace-nowrap text-fg-muted`}>{new Date(r.recorded_at).toLocaleString(undefined, { dateStyle: 'medium', timeStyle: 'short' })}</td>
                <td className={`${td} text-fg`}>{topicName(r.topic_id)}</td>
                <td className={`${td} w-24`}><ScoreBadge score={r.score} /></td>
              </tr>
            ))}
          </Table>
        )}
      </Card>
    </div>
  );

  return (
    <>
      <PageHeader title="Scores" subtitle={selected ? `Log quiz, test or self-assessed scores for ${selected.name}. Mastery is the average per topic.` : 'Pick a student in the top bar.'} />
      {body}
    </>
  );
}
