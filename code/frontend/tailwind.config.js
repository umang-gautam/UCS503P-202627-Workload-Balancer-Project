/** @type {import('tailwindcss').Config} */
// Colours are CSS variables (see src/index.css) so the dark theme is a variable swap.
const v = (name) => `rgb(var(--${name}) / <alpha-value>)`;

export default {
  content: ["./index.html", "./src/**/*.{js,jsx}"],
  darkMode: 'class',
  theme: {
    extend: {
      fontFamily: { sans: ['Poppins', 'ui-sans-serif', 'system-ui', 'sans-serif'] },
      colors: {
        page: v('page'),
        surface: { DEFAULT: v('surface'), 2: v('surface-2'), 3: v('surface-3') },
        edge: { DEFAULT: v('edge'), strong: v('edge-strong') },
        fg: { DEFAULT: v('fg'), muted: v('fg-muted'), subtle: v('fg-subtle') },
        // Thapar LMS palette: maroon primary, steel blue secondary
        brand: { 50: v('brand-50'), 100: v('brand-100'), 600: v('brand-600'), 700: v('brand-700'), 800: v('brand-800') },
        steel: { 600: '#0b5f8a', 700: '#094c6e' },
      },
    },
  },
  plugins: [],
}
