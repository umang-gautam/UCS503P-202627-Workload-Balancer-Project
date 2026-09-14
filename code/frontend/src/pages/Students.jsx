import { useEffect, useState } from 'react';
import {
  createEnrollment, createStudent, deleteEnrollment, deleteStudent,
  fetchEnrollmentsByStudent, fetchSubjects,
} from '../api/client.js';
import { useStudents } from '../context/StudentContext.jsx';
import { Alert, Button, Card, EmptyState, Field, Input, PageHeader, Spinner, Table, td } from '../components/ui.jsx';

export default function Students() {
  const { students, selected, selectedId, setSelectedId, loading, error, reload } = useStudents();
  const [form, setForm] = useState({ name: '', email: '' });
  const [creating, setCreating] = useState(false);
  const [formError, setFormError] = useState(null);
  const [subjects, setSubjects] = useState([]);
  const [enrollments, setEnrollments] = useState([]);
  const [enrolError, setEnrolError] = useState(null);
  const [busySubject, setBusySubject] = useState(null);

  useEffect(() => {
    fetchSubjects().then((s) => setSubjects(s || [])).catch((e) => setEnrolError(e.message));
  }, []);

  const loadEnrollments = async (id) => {
    if (!id) { setEnrollments([]); return; }
    try {
      setEnrollments((await fetchEnrollmentsByStudent(id)) || []);
      setEnrolError(null);
    } catch (e) {
      setEnrolError(e.message);
    }
  };
  useEffect(() => { loadEnrollments(selectedId); }, [selectedId]);

  const submit = async (e) => {
    e.preventDefault();
    setCreating(true);
    setFormError(null);
    try {
      const created = await createStudent(form);
      setForm({ name: '', email: '' });
      await reload();
      setSelectedId(created.id);
    } catch (err) {
      setFormError(err.message);
    } finally {
      setCreating(false);
    }
  };

  const remove = async (student) => {
    if (!window.confirm(`Delete ${student.name}? Their enrolments, scores and plans go with them.`)) return;
    try {
      await deleteStudent(student.id);
      await reload();
    } catch (err) {
      setFormError(err.message);
    }
  };

  const toggle = async (subject) => {
    const existing = enrollments.find((en) => en.subject_id === subject.id);
    setBusySubject(subject.id);
    try {
      if (existing) await deleteEnrollment(existing.id);
      else await createEnrollment({ student_id: selectedId, subject_id: subject.id });
      await loadEnrollments(selectedId);
    } catch (err) {
      setEnrolError(err.message);
    } finally {
      setBusySubject(null);
    }
  };

  return (
    <>
      <PageHeader title="Students" subtitle="Who is being planned for, and which subjects each of them takes." />
      {error && <Alert kind="error" onRetry={reload} className="mb-4">{error}</Alert>}
      <div className="grid gap-4 lg:grid-cols-3">
        <div className="lg:col-span-2">
          <Card title="All students" padded={false}>
            {loading ? <Spinner /> : students.length === 0 ? (
              <div className="p-4"><EmptyState title="No students yet">Add one with the form.</EmptyState></div>
            ) : (
              <Table head={['Name', 'Email', '']}>
                {students.map((s) => (
                  <tr key={s.id} className={s.id === selectedId ? 'bg-brand-50' : ''}>
                    <td className={`${td} font-medium text-gray-900`}>{s.name}</td>
                    <td className={`${td} text-gray-600`}>{s.email}</td>
                    <td className={`${td} text-right whitespace-nowrap`}>
                      {s.id !== selectedId && (
                        <Button variant="ghost" size="sm" onClick={() => setSelectedId(s.id)}>Select</Button>
                      )}
                      <Button variant="danger" size="sm" className="ml-2" onClick={() => remove(s)}>Delete</Button>
                    </td>
                  </tr>
                ))}
              </Table>
            )}
          </Card>
        </div>

        <div className="space-y-4">
          <Card title="Add student">
            <form onSubmit={submit} className="space-y-3">
              <Field label="Name" htmlFor="st-name">
                <Input id="st-name" required value={form.name} onChange={(e) => setForm({ ...form, name: e.target.value })} />
              </Field>
              <Field label="Email" htmlFor="st-email">
                <Input id="st-email" type="email" required value={form.email} onChange={(e) => setForm({ ...form, email: e.target.value })} />
              </Field>
              {formError && <Alert kind="error">{formError}</Alert>}
              <Button type="submit" disabled={creating}>{creating ? 'Adding…' : 'Add student'}</Button>
            </form>
          </Card>

          <Card title={selected ? `Enrolments · ${selected.name}` : 'Enrolments'}>
            {!selected ? (
              <p className="text-sm text-gray-500">Select a student to manage enrolments.</p>
            ) : subjects.length === 0 ? (
              <p className="text-sm text-gray-500">No subjects exist yet. Create them under Subjects.</p>
            ) : (
              <ul className="divide-y divide-gray-100">
                {subjects.map((sub) => {
                  const on = enrollments.some((en) => en.subject_id === sub.id);
                  return (
                    <li key={sub.id} className="flex items-center justify-between py-2">
                      <label className="flex items-center gap-3 text-sm">
                        <input
                          type="checkbox"
                          className="h-4 w-4 rounded border-gray-300 text-brand-700 focus:ring-brand-600"
                          checked={on}
                          disabled={busySubject === sub.id}
                          onChange={() => toggle(sub)}
                        />
                        <span>
                          <span className="font-medium text-gray-900">{sub.code}</span>
                          <span className="ml-2 text-gray-600">{sub.name}</span>
                        </span>
                      </label>
                    </li>
                  );
                })}
              </ul>
            )}
            {enrolError && <Alert kind="error" className="mt-3">{enrolError}</Alert>}
          </Card>
        </div>
      </div>
    </>
  );
}
