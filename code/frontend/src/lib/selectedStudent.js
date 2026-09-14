// Remember which student is selected across pages and reloads.
const KEY = 'wb.selectedStudentId';

export function getStoredStudentId() {
  try { return localStorage.getItem(KEY) || ''; } catch { return ''; }
}

export function storeStudentId(id) {
  try { id ? localStorage.setItem(KEY, id) : localStorage.removeItem(KEY); } catch { /* private mode */ }
}

/** Keep `current` if it is still in `list`, otherwise fall back to the first student. */
export function pickStudentId(list, current) {
  if (list.some((s) => s.id === current)) return current;
  return list.length ? list[0].id : '';
}
