/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './layouts/**/*.html',
    './content/**/*.md',
    './assets/js/**/*.js',
  ],
  theme: {
    extend: {
      colors: {
        primary: '#0B1F3B',
        accent: '#2AA198',
        neutral: '#F5F7FA',
      },
      fontFamily: {
        'headings': ['Spectral', 'serif'],
        'body': ['Inter', 'sans-serif'],
      },
      borderRadius: {
        'theme': '1rem',
      },
      boxShadow: {
        'theme': '0 10px 20px rgba(0,0,0,0.06)',
      }
    },
  },
  plugins: [],
}