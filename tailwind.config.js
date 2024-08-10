const defaultConfig = /** @type {import('tailwindcss').Config} */
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

defaultConfig.content = [
    "app.py",
    "fluidframe/core/components.py",
    "fluidframe/components/**/*.py",
    "fluidframe/templates/index.html"
];

/** @type {import('tailwindcss').Config} */
module.exports = {
  ...defaultConfig,
  content: [
    ...defaultConfig.content,
    // Add your custom content paths here
  ],
  theme: {
    ...defaultConfig.theme,
    extend: {
      // Add your custom theme extensions here
    },
  },
  plugins: [
    ...defaultConfig.plugins,
    // Add your custom plugins here
  ],
}
