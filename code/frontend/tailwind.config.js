/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,jsx}"],
  theme: {
    extend: {
      fontFamily: { sans: ['Poppins', 'ui-sans-serif', 'system-ui', 'sans-serif'] },
      colors: {
        // Thapar LMS palette: maroon primary, steel blue secondary
        brand: { 50: '#fbf1f1', 100: '#f5dcdc', 600: '#a11212', 700: '#8b0000', 800: '#6d0000' },
        steel: { 600: '#0b5f8a', 700: '#094c6e' },
        page: '#f4f5f7',
      },
    },
  },
  plugins: [],
}
