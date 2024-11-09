// tailwind.config.js
module.exports = {
  content: [
    './app/templates/**/*.html',
    './app/static/js/**/*.js',
    './app/templates/**/**/*.html', // Include deeper nested templates
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#EBEDF2',
          100: '#C5CCD9',
          200: '#9EAABF',
          300: '#7888A6',
          400: '#51678C',
          500: '#2B4573',
          600: '#182140',
          700: '#131A33',
          800: '#0F172A',
          900: '#0A0D1A',
        },
        secondary: {
          50: '#FCE4BB',
          100: '#FBDCA8',
          200: '#FACD81',
          300: '#F8BD59',
          400: '#F7AE32',
          500: '#F59E0B',
          600: '#C07C08',
          700: '#8A5906',
          800: '#543603',
          900: '#1E1401',
          950: '#030200',
        },
        white: {
          0: '#FFFFFF',
          50: '#EAEAEA',
          100: '#FDFDFD',
          200: '#FBFBFB',
          300: '#FAFAFA',
          400: '#F8F8F8',
          500: '#F7F7F7',
          600: '#D9D9D9',
          700: '#BDBDBD',
          800: '#A0A0A0',
          900: '#838383',
        },
      },
    },
  },
  plugins: [],
}
