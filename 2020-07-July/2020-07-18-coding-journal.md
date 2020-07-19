# Nuxt Auth Module

I will be following these 3 resources for nuxt auth module

- [Official documentation](https://auth.nuxtjs.org/#getting-started)

- [Article on implementing Auth in Nuxt](https://www.digitalocean.com/community/tutorials/implementing-authentication-in-nuxtjs-app)

- [Youtube video by Vue Screecasts](https://www.youtube.com/watch?v=zzUpO8tXoaw&feature=youtu.be)


## Install auth module with npm

`npm install @nuxtjs/auth @nuxtjs/axios`

Edit `nuxt.config.js`

```
modules: [
  '@nuxtjs/axios',
  '@nuxtjs/auth'
],
auth: {
  strategies: {
    local: {
      endpoints: {
        login: { url: 'login', method: 'post', propertyName: 'data.token' },
        logout: false
      }
    }
  }
}
```

This will allow us to use `$auth.user` and `$auth.loggedIn` within our components.

using `$auth.loginWith`

```
async onSubmit() {
  await this.$auth.loginWith('local', {
    data: {
      username: this.username,
      password: this.password
    }
  })
}
```

Can also use refresh scheme to work with jwt refresh token. [Official documentation](https://dev.auth.nuxtjs.org/schemes/refresh.html)