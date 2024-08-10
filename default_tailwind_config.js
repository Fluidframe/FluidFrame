/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app.py",
    "./fluidframe/core/components.py",
    "./fluidframe/components/**/*.py",
    "./fluidframe/templates/index.html",
  ],
  safelist: [
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}