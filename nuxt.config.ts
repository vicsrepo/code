export default defineNuxtConfig({
  app: {
    payload: {
      replacer: (key, value) => {
        if (typeof value === 'function') {
          return undefined;
        }
        return value;
      }
    }
  },

  // https://github.com/nuxt-themes/docus
  extends: ['@nuxt-themes/docus'],
  devtools: { enabled: true },

  modules: [
    // Remove it if you don't use Plausible analytics
    // https://github.com/nuxt-modules/plausible
    '@nuxtjs/plausible'
  ],
  compatibilityDate: '2024-10-24'
})
