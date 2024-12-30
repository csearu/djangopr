const colors = require('tailwindcss/colors')
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./myapp/templates/myapp/index.html",
    "./src/pages/**/*.{js,ts,jsx,tsx}",
    "./src/components/**/*.{js,ts,jsx,tsx}",
    "./src/**/*.{html,js}",
    "./app/**/*.{js,ts,jsx,tsx}",
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",

    // Or if using `src` directory:
    "./src/**/*.{js,ts,jsx,tsx}",
  ],

  theme: {
    extend: {
        colors: {
          transparent: 'transparent',
          current: 'currentColor',
          black: colors.black,
          white: colors.white,
          emerald: colors.emerald,
          indigo: colors.indigo,
          yellow: colors.yellow,
          stone: colors.warmGray,
          sky: colors.lightBlue,
          neutral: colors.trueGray,
          gray: colors.coolGray,
          slate: colors.blueGray,
          lime: colors.lime,
          rose: colors.rose,
        },
    },
},
  plugins: [],
}
