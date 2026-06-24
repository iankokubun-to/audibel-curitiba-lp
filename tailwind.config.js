module.exports = {
  content: ["./index.html", "./js/**/*.js"],
  theme: {
    extend: {
      colors: {
        audibel: {
          red: '#A91F20',
          gray: '#404040',
          lightGray: '#F5F5F5',
          white: '#FFFFFF'
        }
      },
      fontFamily: {
        barlow: ['"Barlow Condensed"', 'sans-serif'],
        sans: ['"Open Sans"', 'sans-serif'],
      },
      borderRadius: {
        'brand': '1.5rem',
      }
    }
  }
}
