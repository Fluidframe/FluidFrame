/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
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

