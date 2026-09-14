/**
 * API client — single source of truth for all backend calls.
 *
 * Every component imports from here instead of writing its own fetch().
 *
 * Base URL: VITE_API_BASE if set at build time, otherwise '/api', which the
 * Vite dev server and the nginx container both proxy to the backend. Set
 * VITE_API_BASE only for hosting where no proxy sits in front (e.g. a
 * static host talking to a separately deployed backend).
 */

const BASE = (import.meta.env.VITE_API_BASE || '/api').replace(/\/$/, '');

async function request(path, options = {}) {
  const url = `${BASE}${path}`;
  let res;
  try {
    res = await fetch(url, {
      headers: { 'Content-Type': 'application/json', ...options.headers },
      ...options,
    });
  } catch {
    throw new Error('Cannot reach the backend. Is it running?');
  }

  if (res.status === 204) return null; // DELETE returns no content

  // Parse JSON only when the server says it is JSON. A proxy error page or a
  // plain-text 500 must become a readable message, not a JSON.parse crash.
  const text = await res.text();
  const isJson = (res.headers.get('content-type') || '').includes('application/json');
  let data = null;
  if (isJson && text) {
    try { data = JSON.parse(text); } catch { data = null; }
  }

  if (!res.ok) {
    const detail = data && (data.detail ?? data.message);
    const msg = detail == null
      ? (text ? text.slice(0, 200) : `Request failed: ${res.status}`)
      : typeof detail === 'string' ? detail : JSON.stringify(detail);
    throw new Error(msg);
  }

  return data;
}

// ── Students ────────────────────────────────────────────────
export const fetchStudents   = ()            => request('/students/');
export const fetchStudent    = (id)          => request(`/students/${id}`);
export const createStudent   = (body)        => request('/students/', { method: 'POST', body: JSON.stringify(body) });
export const updateStudent   = (id, body)    => request(`/students/${id}`, { method: 'PATCH', body: JSON.stringify(body) });
export const deleteStudent   = (id)          => request(`/students/${id}`, { method: 'DELETE' });
export const fetchStudentScores = (id)       => request(`/students/${id}/scores`);

// ── Subjects ────────────────────────────────────────────────
export const fetchSubjects   = ()            => request('/subjects/');
export const fetchSubject    = (id)          => request(`/subjects/${id}`);
export const createSubject   = (body)        => request('/subjects/', { method: 'POST', body: JSON.stringify(body) });
export const updateSubject   = (id, body)    => request(`/subjects/${id}`, { method: 'PATCH', body: JSON.stringify(body) });
export const deleteSubject   = (id)          => request(`/subjects/${id}`, { method: 'DELETE' });

// ── Topics ──────────────────────────────────────────────────
export const fetchTopics        = ()         => request('/topics/');
export const fetchTopicsBySubject = (subId)  => request(`/topics/by-subject/${subId}`);
export const createTopic        = (body)     => request('/topics/', { method: 'POST', body: JSON.stringify(body) });
export const deleteTopic        = (id)       => request(`/topics/${id}`, { method: 'DELETE' });

// ── Assignments ─────────────────────────────────────────────
export const fetchAssignments       = ()        => request('/assignments/');
export const fetchAssignmentsByTopic = (topicId) => request(`/assignments/by-topic/${topicId}`);
export const createAssignment       = (body)    => request('/assignments/', { method: 'POST', body: JSON.stringify(body) });
export const deleteAssignment       = (id)      => request(`/assignments/${id}`, { method: 'DELETE' });

// ── Enrollments ─────────────────────────────────────────────
export const fetchEnrollments          = ()       => request('/enrollments/');
export const fetchEnrollmentsByStudent = (stuId)  => request(`/enrollments/by-student/${stuId}`);
export const createEnrollment          = (body)   => request('/enrollments/', { method: 'POST', body: JSON.stringify(body) });
export const deleteEnrollment          = (id)     => request(`/enrollments/${id}`, { method: 'DELETE' });

// ── Performance ─────────────────────────────────────────────
export const createPerformanceRecord = (body) => request('/performance/', { method: 'POST', body: JSON.stringify(body) });
export const fetchPerformanceByStudent = (stuId) => request(`/performance/by-student/${stuId}`);

// ── Study Plans ─────────────────────────────────────────────
export const generatePlan    = (body)        => request('/study-plans/generate', { method: 'POST', body: JSON.stringify(body) });
export const fetchPlan       = (id)          => request(`/study-plans/${id}`);
export const fetchPlansByStudent = (stuId)   => request(`/study-plans/by-student/${stuId}`);

// ── Study Sessions ──────────────────────────────────────────
export const fetchSessionsByPlan = (planId)  => request(`/study-sessions/by-plan/${planId}`);
export const updateSession       = (id, body) => request(`/study-sessions/${id}`, { method: 'PATCH', body: JSON.stringify(body) });

// ── Agent ───────────────────────────────────────────────────
export const triggerRebalance = (body) => request('/agent/rebalance', { method: 'POST', body: JSON.stringify(body) });

// ── Demo ────────────────────────────────────────────────────
export const seedDemoData = () => request('/demo/seed', { method: 'POST' });
