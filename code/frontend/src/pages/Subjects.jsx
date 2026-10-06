import { useEffect, useState } from 'react';
import {
  createAssignment, createSubject, createTopic, deleteAssignment, deleteSubject, deleteTopic,
  fetchAssignments, fetchSubjects, fetchTopics,
} from '../api/client.js';
import { Alert, Button, Card, EmptyState, Field, Input, PageHeader, Spinner, Table, formatDate, td } from '../components/ui.jsx';

function DeadlineForm({ topicId, onAdd }) {
  const [title, setTitle] = useState('');
  const [due, setDue] = useState('');
  const [busy, setBusy] = useState(false);
  const submit = async (e) => {
    e.preventDefault();
    setBusy(true);
    try {
      await onAdd({ topic_id: topicId, title, due_date: due });
      setTitle('');
      setDue('');
    } finally {
      setBusy(false);
    }
  };
  return (
    <form onSubmit={submit} className="mt-2 flex flex-wrap items-center gap-2">
      <Input placeholder="New deadline" required value={title} onChange={(e) => setTitle(e.target.value)} className="!w-40 !py-1 text-xs" />
      <Input type="date" required value={due} onChange={(e) => setDue(e.target.value)} className="!w-36 !py-1 text-xs" />
      <Button type="submit" size="sm" variant="secondary" disabled={busy}>Add</Button>
    </form>
  );
}

export default function Subjects() {
  const [subjects, setSubjects] = useState([]);
  const [topics, setTopics] = useState([]);
  const [assignments, setAssignments] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [form, setForm] = useState({ code: '', name: '' });
  const [creating, setCreating] = useState(false);
  const [newTopic, setNewTopic] = useState({});
  const [searchTerm, setSearchTerm] = useState('');
  const filteredSubjects = subjects.filter((s) =>
    s.code.toLowerCase().includes(searchTerm.toLowerCase()) ||
    s.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const load = async () => {
    setLoading(true);
    setError(null);
    try {
      const [s, t, a] = await Promise.all([fetchSubjects(), fetchTopics(), fetchAssignments()]);
      setSubjects(s || []);
      setTopics(t || []);
      setAssignments(a || []);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };
  useEffect(() => { load(); }, []);

  const run = async (fn) => {
    setError(null);
    try { await fn(); await load(); } catch (err) { setError(err.message); }
  };

  const addSubject = (e) => {
    e.preventDefault();
    setCreating(true);
    run(async () => { await createSubject(form); setForm({ code: '', name: '' }); }).finally(() => setCreating(false));
  };
  const addTopic = (subjectId) => (e) => {
    e.preventDefault();
    const name = (newTopic[subjectId] || '').trim();
    if (!name) return;
    run(async () => { await createTopic({ subject_id: subjectId, name }); setNewTopic({ ...newTopic, [subjectId]: '' }); });
  };
  const removeSubject = (s) => window.confirm(`Delete ${s.code}? Its topics, deadlines and scores go with it.`) && run(() => deleteSubject(s.id));
  const removeTopic = (t) => window.confirm(`Delete topic "${t.name}"?`) && run(() => deleteTopic(t.id));

  return (
    <>
      <PageHeader title="Subjects" subtitle="The shared catalogue: subjects, their topics, and the deadlines that drive urgency." />
      {error && <Alert kind="error" onRetry={load} className="mb-4">{error}</Alert>}
      <div className="grid gap-4 lg:grid-cols-3">
        <div className="space-y-4 lg:col-span-2">
          {subjects.length > 0 && (
            <div className="mb-2">
              <Input
                placeholder="Search subjects by code or name (e.g. UCS503, Operating System)..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="!py-2 w-full"
              />
            </div>
          )}
          {loading ? <Spinner /> : subjects.length === 0 ? (
            <EmptyState title="No subjects yet">Create the first one with the form.</EmptyState>
          ) : filteredSubjects.map((s) => {
            const subjectTopics = topics.filter((t) => t.subject_id === s.id);
            return (
              <Card
                key={s.id}
                title={<span><span className="text-brand-700">{s.code}</span> · {s.name}</span>}
                actions={<Button variant="danger" size="sm" onClick={() => removeSubject(s)}>Delete subject</Button>}
                padded={false}
              >
                {subjectTopics.length === 0 ? (
                  <p className="px-4 py-3 text-sm text-fg-subtle">No topics yet.</p>
                ) : (
                  <Table head={['Topic', 'Deadlines', '']}>
                    {subjectTopics.map((t) => {
                      const due = assignments.filter((a) => a.topic_id === t.id).sort((a, b) => a.due_date.localeCompare(b.due_date));
                      return (
                        <tr key={t.id}>
                          <td className={`${td} w-56 font-medium text-fg`}>{t.name}</td>
                          <td className={td}>
                            {due.length === 0 && <span className="text-xs text-fg-subtle">None</span>}
                            <ul className="space-y-1">
                              {due.map((a) => (
                                <li key={a.id} className="flex items-center gap-2 text-xs">
                                  <span className="text-fg-muted">{a.title}</span>
                                  <span className="text-fg-subtle">{formatDate(a.due_date)}</span>
                                  <button type="button" onClick={() => run(() => deleteAssignment(a.id))} className="text-fg-subtle hover:text-red-600 dark:hover:text-red-400" aria-label={`Remove ${a.title}`}>×</button>
                                </li>
                              ))}
                            </ul>
                            <DeadlineForm topicId={t.id} onAdd={(body) => run(() => createAssignment(body))} />
                          </td>
                          <td className={`${td} w-20 text-right`}>
                            <Button variant="danger" size="sm" onClick={() => removeTopic(t)}>Delete</Button>
                          </td>
                        </tr>
                      );
                    })}
                  </Table>
                )}
                <form onSubmit={addTopic(s.id)} className="flex items-center gap-2 border-t border-edge bg-surface-2 px-4 py-2.5">
                  <Input placeholder="New topic name" value={newTopic[s.id] || ''} onChange={(e) => setNewTopic({ ...newTopic, [s.id]: e.target.value })} className="!w-64 !py-1.5" />
                  <Button type="submit" size="sm" variant="secondary">Add topic</Button>
                </form>
              </Card>
            );
          })}
        </div>

        <Card title="Add subject" className="self-start">
          <form onSubmit={addSubject} className="space-y-3">
            <Field label="Code" htmlFor="sub-code" hint="e.g. UCS503">
              <Input id="sub-code" required value={form.code} onChange={(e) => setForm({ ...form, code: e.target.value.toUpperCase() })} />
            </Field>
            <Field label="Name" htmlFor="sub-name">
              <Input id="sub-name" required value={form.name} onChange={(e) => setForm({ ...form, name: e.target.value })} />
            </Field>
            <Button type="submit" disabled={creating}>{creating ? 'Adding…' : 'Add subject'}</Button>
          </form>
        </Card>
      </div>
    </>
  );
}
