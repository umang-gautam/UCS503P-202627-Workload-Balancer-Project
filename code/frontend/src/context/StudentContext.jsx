import { createContext, useCallback, useContext, useEffect, useState } from 'react';
import { fetchStudents } from '../api/client.js';
import { getStoredStudentId, pickStudentId, storeStudentId } from '../lib/selectedStudent.js';

const StudentContext = createContext(null);

/**
 * One selected student for the whole app, chosen in the top bar and
 * remembered in localStorage. Pages read it with useStudents().
 */
export function StudentProvider({ children }) {
  const [students, setStudents] = useState([]);
  const [selectedId, setSelectedId] = useState(getStoredStudentId);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const reload = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const list = (await fetchStudents()) || [];
      setStudents(list);
      setSelectedId((current) => pickStudentId(list, current));
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => { reload(); }, [reload]);
  useEffect(() => { storeStudentId(selectedId); }, [selectedId]);

  const selected = students.find((s) => s.id === selectedId) || null;

  return (
    <StudentContext.Provider value={{ students, selected, selectedId, setSelectedId, loading, error, reload }}>
      {children}
    </StudentContext.Provider>
  );
}

export function useStudents() {
  return useContext(StudentContext);
}
