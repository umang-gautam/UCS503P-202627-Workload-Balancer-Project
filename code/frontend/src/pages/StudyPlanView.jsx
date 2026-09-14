import { Fragment, useEffect, useMemo, useState } from 'react';
import { fetchPlansByStudent, fetchTopics, generatePlan, triggerRebalance } from '../api/client.js';
import { useStudents } from '../context/StudentContext.jsx';
import useStudyPlan from '../hooks/useStudyPlan.js';
import SessionBlock from '../components/SessionBlock.jsx';
import { Alert, Button, Card, EmptyState, Field, Input, PageHeader, Select, Spinner, Table, formatDate } from '../components/ui.jsx';

const today = () => new Date().toISOString().slice(0, 10);

export default function StudyPlanView() {
  const { selected, selectedId, students, loading: loadingStudents } = useStudents();
  const plan = useStudyPlan(selectedId);
  const [topicMap, setTopicMap] = useState({});
  const [form, setForm] = useState({ hours_per_day: 2, num_days: 7, start_date: today() });
  const [generating, setGenerating] = useState(false);
  const [genError, setGenError] = useState(null);
  const [rebalancing, setRebalancing] = useState(false);
  const [rebalance, setRebalance] = useState(null); // { text, changesNeeded } | { error }

  useEffect(() => {
    fetchTopics().then((t) => setTopicMap(Object.fromEntries((t || []).map((x) => [x.id, x.name])))).catch(() => {});
  }, []);
  useEffect(() => { setRebalance(null); setGenError(null); }, [selectedId]);

  const absorb = (result) => {
    if (Array.isArray(result?.topic_scores)) {
      setTopicMap((m) => ({ ...m, ...Object.fromEntries(result.topic_scores.map((t) => [t.topic_id, t.topic_name])) }));
    }
    if (result?.plan_id) plan.setSelectedPlanId(result.plan_id);
    if (Array.isArray(result?.sessions)) plan.setSessions(result.sessions);
  };

  const generate = async (e) => {
    e.preventDefault();
    setGenerating(true);
    setGenError(null);
    try {
      const result = await generatePlan({ student_id: selectedId, hours_per_day: Number(form.hours_per_day), num_days: Number(form.num_days), start_date: form.start_date || today() });
      absorb(result);
      plan.setStudentPlans((await fetchPlansByStudent(selectedId)) || []);
    } catch (err) {
      setGenError(err.message);
    } finally {
      setGenerating(false);
    }
  };

  const runRebalance = async () => {
    setRebalancing(true);
    try {
      const r = await triggerRebalance({ student_id: selectedId, trigger: 'manual' });
      setRebalance({ text: r.explanation, changesNeeded: r.changes_needed });
      if (r.new_plan) {
        absorb(r.new_plan);
        plan.setStudentPlans((await fetchPlansByStudent(selectedId)) || []);
      }
    } catch (err) {
      setRebalance({ error: err.message });
    } finally {
      setRebalancing(false);
    }
  };

  const byDate = useMemo(() => {
    const groups = {};
    [...plan.sessions].sort((a, b) => a.date.localeCompare(b.date)).forEach((s) => { (groups[s.date] ||= []).push(s); });
    return Object.entries(groups);
  }, [plan.sessions]);

  const sortedPlans = [...plan.studentPlans].sort((a, b) => (b.start_date || '').localeCompare(a.start_date || ''));
  const current = sortedPlans.find((p) => p.id === plan.selectedPlanId);
  const done = plan.sessions.filter((s) => s.status === 'done').length;

  if (loadingStudents) return <><PageHeader title="Study plan" /><Spinner /></>;
  if (!selectedId) return <><PageHeader title="Study plan" /><EmptyState title="No student selected">{students.length ? 'Pick a student in the top bar.' : 'Add a student first.'}</EmptyState></>;

  return (
    <>
      <PageHeader title="Study plan" subtitle={`Sessions for ${selected?.name}, allocated by priority and rebalanced by the agent when things slip.`} />
      <div className="grid gap-4 lg:grid-cols-3">
        <div className="space-y-4">
          <Card title="Generate a plan">
            <form onSubmit={generate} className="space-y-3">
              <div className="grid grid-cols-2 gap-3">
                <Field label="Hours per day" htmlFor="hpd">
                  <Input id="hpd" type="number" min="1" max="12" step="0.5" required value={form.hours_per_day} onChange={(e) => setForm({ ...form, hours_per_day: e.target.value })} />
                </Field>
                <Field label="Days" htmlFor="days">
                  <Input id="days" type="number" min="1" max="90" required value={form.num_days} onChange={(e) => setForm({ ...form, num_days: e.target.value })} />
                </Field>
              </div>
              <Field label="Start date" htmlFor="start">
                <Input id="start" type="date" value={form.start_date} onChange={(e) => setForm({ ...form, start_date: e.target.value })} />
              </Field>
              {genError && <Alert kind="error">{genError}</Alert>}
              <Button type="submit" disabled={generating} className="w-full">{generating ? 'Generating…' : 'Generate plan'}</Button>
              <p className="text-xs text-fg-subtle">Time is split across topics in proportion to priority, in 30–60 minute sessions.</p>
            </form>
          </Card>

          <Card title="Rebalance">
            <p className="mb-3 text-sm text-fg-muted">Re-score every topic with the latest scores and deadlines and rebuild the remaining sessions.</p>
            <Button variant="secondary" onClick={runRebalance} disabled={rebalancing || plan.studentPlans.length === 0} className="w-full">
              {rebalancing ? 'Rebalancing…' : 'Run the agent'}
            </Button>
            {rebalance?.error && <Alert kind="error" className="mt-3">{rebalance.error}</Alert>}
            {rebalance?.text && <Alert kind={rebalance.changesNeeded ? 'info' : 'success'} className="mt-3 font-mono text-xs">{rebalance.text}</Alert>}
          </Card>
        </div>

        <div className="lg:col-span-2">
          <Card
            title={current ? `Sessions · ${formatDate(current.start_date)} – ${formatDate(current.end_date)}` : 'Sessions'}
            actions={sortedPlans.length > 1 && (
              <Select value={plan.selectedPlanId} onChange={(e) => plan.selectPlan(e.target.value)} className="!w-64 !py-1 text-xs">
                {sortedPlans.map((p, i) => (
                  <option key={p.id} value={p.id}>{i === 0 ? 'Latest' : 'Plan'} · {formatDate(p.start_date)} – {formatDate(p.end_date)}</option>
                ))}
              </Select>
            )}
            padded={false}
          >
            {plan.loadingSessions ? <Spinner label="Loading sessions…" /> : plan.sessionsError ? (
              <div className="p-4"><Alert kind="error" onRetry={() => plan.loadPlanSessions(plan.selectedPlanId)}>{plan.sessionsError}</Alert></div>
            ) : plan.sessions.length === 0 ? (
              <div className="p-4"><EmptyState title="No plan yet">Generate one on the left. Topics need at least one enrolment and score or deadline to be scheduled.</EmptyState></div>
            ) : (
              <>
                <div className="flex items-center justify-between border-b border-edge bg-surface-2 px-4 py-2 text-xs text-fg-muted">
                  <span>{plan.sessions.length} sessions · {done} done</span>
                  <span>{plan.sessions.reduce((a, s) => a + s.duration_minutes, 0)} minutes total</span>
                </div>
                <Table head={['Topic', 'Duration', 'Status']}>
                  {byDate.map(([date, sessions]) => (
                    <Fragment key={date}>
                      <tr className="bg-surface-2">
                        <td colSpan={3} className="px-4 py-1.5 text-xs font-semibold uppercase tracking-wide text-brand-700">
                          {new Date(date).toLocaleDateString(undefined, { weekday: 'long', day: 'numeric', month: 'short' })}
                          <span className="ml-2 font-normal normal-case tracking-normal text-fg-subtle">{sessions.reduce((a, x) => a + x.duration_minutes, 0)} min</span>
                        </td>
                      </tr>
                      {sessions.map((x) => (
                        <SessionBlock key={x.id} session={x} topicName={topicMap[x.topic_id] || x.topic_id} isUpdating={plan.updatingSessionId === x.id} onStatusChange={plan.setSessionStatus} />
                      ))}
                    </Fragment>
                  ))}
                </Table>
              </>
            )}
          </Card>
        </div>
      </div>
    </>
  );
}
