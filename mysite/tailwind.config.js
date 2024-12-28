/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./myapp/templates/myapp/index.html",
    "./src/pages/**/*.{js,ts,jsx,tsx}",
    "./src/components/**/*.{js,ts,jsx,tsx}",
  ],

  theme: {
    extend: {},
  },
  plugins: [],
}

