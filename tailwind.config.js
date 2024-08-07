/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app.py",
    "./fluidframe/components/**/*.py",
    "./fluidframe/templates/index.html",
  ],
  safelist: [
    "relative"
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}