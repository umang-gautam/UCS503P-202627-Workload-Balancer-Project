import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { fetchStudentScores, seedDemoData } from '../api/client.js';
import { useStudents } from '../context/StudentContext.jsx';
import TopicRow from '../components/TopicRow.jsx';
import { Alert, Button, Card, EmptyState, PageHeader, Spinner, Table } from '../components/ui.jsx';

function Stat({ label, value, hint }) {
  return (
    <Card>
      <div className="text-xs font-medium uppercase tracking-wide text-fg-subtle">{label}</div>
      <div className="mt-1 text-2xl font-semibold text-fg">{value}</div>
      {hint && <div className="mt-0.5 text-xs text-fg-subtle">{hint}</div>}
    </Card>
  );
}

export default function Dashboard() {
  const { students, selected, selectedId, loading: loadingStudents, error: studentsError, reload } = useStudents();
  const [scores, setScores] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [seeding, setSeeding] = useState(false);
  const [seedError, setSeedError] = useState(null);

  const loadScores = async (id) => {
    if (!id) { setScores([]); return; }
    setLoading(true);
    setError(null);
    try {
      setScores((await fetchStudentScores(id)) || []);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => { loadScores(selectedId); }, [selectedId]);

  const seed = async () => {
    setSeeding(true);
    setSeedError(null);
    try {
      await seedDemoData();
      await reload();
    } catch (err) {
      setSeedError(err.message);
    } finally {
      setSeeding(false);
    }
  };

  const urgent = scores.filter((t) => t.priority > 70).length;
  const avgMastery = scores.length ? Math.round((scores.reduce((a, t) => a + t.mastery, 0) / scores.length) * 100) : 0;
  const avgUrgency = scores.length ? Math.round((scores.reduce((a, t) => a + t.urgency, 0) / scores.length) * 100) : 0;

  let body;
  if (studentsError) {
    body = <Alert kind="error" onRetry={reload}>{studentsError}</Alert>;
  } else if (loadingStudents) {
    body = <Spinner label="Loading students…" />;
  } else if (students.length === 0) {
    body = (
      <EmptyState
        title="No students yet"
        action={
          <div className="flex flex-wrap items-center justify-center gap-2">
            <Button onClick={seed} disabled={seeding}>{seeding ? 'Loading demo data…' : 'Load demo data'}</Button>
            <Link to="/students"><Button variant="secondary">Add a student</Button></Link>
          </div>
        }
      >
        Load a demo dataset with two students, three subjects, deadlines and scores, or add students and subjects yourself.
        {seedError && <span className="mt-2 block text-red-700 dark:text-red-300">{seedError}</span>}
      </EmptyState>
    );
  } else if (loading) {
    body = <Spinner label="Scoring topics…" />;
  } else if (error) {
    body = <Alert kind="error" onRetry={() => loadScores(selectedId)}>{error}</Alert>;
  } else if (scores.length === 0) {
    body = (
      <EmptyState title="No enrolled topics" action={<Link to="/students"><Button variant="secondary">Manage enrolments</Button></Link>}>
        {selected?.name} is not enrolled in any subject with topics yet.
      </EmptyState>
    );
  } else {
    body = (
      <>
        <div className="mb-4 grid grid-cols-2 gap-4 lg:grid-cols-4">
          <Stat label="Topics" value={scores.length} />
          <Stat label="Urgent" value={urgent} hint="priority above 70" />
          <Stat label="Average mastery" value={`${avgMastery}%`} />
          <Stat label="Average urgency" value={`${avgUrgency}%`} />
        </div>
        <Card title="Priority queue" padded={false}>
          <Table head={['#', 'Topic', 'Priority', 'Mastery', 'Urgency']}>
            {scores.map((t, i) => <TopicRow key={t.topic_id} topic={t} rank={i + 1} />)}
          </Table>
        </Card>
      </>
    );
  }

  return (
    <>
      <PageHeader
        title="Dashboard"
        subtitle={selected ? `What ${selected.name} should study first, ranked by weakness and deadline pressure.` : 'Pick a student in the top bar.'}
      />
      {body}
    </>
  );
}
