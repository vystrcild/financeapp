const defaultTheme = require('tailwindcss/defaultTheme')
const colors = require('tailwindcss/colors')

module.exports = {
    future: {
        // removeDeprecatedGapUtilities: true,
        // purgeLayersByDefault: true,
    },
    purge: [],
    theme: {
        // colors: colors,
        extend: {
            colors: {
                'virtus-nav': '#2f3242',
                'virtus-back': '#2b2d3c',
                'virtus-primary': '#2481ce',
                'virtus-secondary': '#2196f3',
                'virtus-header': '#3a3e52',
                'virtus-green': '#4caf50',
                'virtus-red': '#f44336',
                'virtus-gray': '#505464',
                'virtus-menu': '#757da3',
        },
            fontFamily: {
                sans: ['Roboto', ...defaultTheme.fontFamily.sans],
            },
        },
    },
    variants: {},
    plugins: [
        require('@tailwindcss/forms'),
    ],
}
