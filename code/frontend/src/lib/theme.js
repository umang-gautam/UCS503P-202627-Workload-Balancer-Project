// Light / dark theme. Order of precedence: ?theme= in the URL, the saved
// choice, then the OS preference. Applied as a `dark` class on <html>.
const KEY = 'wb.theme';

export function getTheme() {
  const fromUrl = new URLSearchParams(window.location.search).get('theme');
  if (fromUrl === 'dark' || fromUrl === 'light') return fromUrl;
  try {
    const saved = localStorage.getItem(KEY);
    if (saved === 'dark' || saved === 'light') return saved;
  } catch { /* private mode */ }
  return window.matchMedia?.('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
}

export function applyTheme(theme) {
  document.documentElement.classList.toggle('dark', theme === 'dark');
  try { localStorage.setItem(KEY, theme); } catch { /* private mode */ }
}
