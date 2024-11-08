// tailwind.config.js
module.exports = {
  content: [
    './app/templates/**/*.html', // Scans all HTML templates in your Flask project
    './app/static/js/**/*.js'     // Optional: Scans any JavaScript files if needed
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
