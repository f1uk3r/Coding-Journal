* [Deploying Vue-CLI project to github pages](https://medium.com/@Roli_Dori/deploy-vue-cli-3-project-to-github-pages-ebeda0705fbd)

1. Create a brance in the project named "gh-pages"

2. Create a `vue.config.js` and paste the following

```
// vue.config.js
module.exports = {
  publicPath: ‘/project-name/’
}
```

3. open the .gitignore file and unignore `/dist` folder

4. run `npm run build`

5. don't commit `.gitignore` and `vue.config.js`

6. run the command `git add dist && git commit -m "commit message"`

7. run the command `git subtree push --prefix dist origin gh-pages`

8. Navigate to `Settings` tab in github.com repository and Scroll to find Github pages section. Select the `gh-pages` branch and click Save.

- [Vue Analytics](https://github.com/MatteoGabriele/vue-analytics) plugin stopped getting new features. So we'll use [vue-gtag](https://github.com/MatteoGabriele/vue-gtag)

- Follow [this link](https://support.google.com/analytics/answer/10269537) carefully to create Universal Analytics property that gives us Trackind ID like this `UA-xxxxxx-1`

- [vue-gtag documentation](https://matteo-gabriele.gitbook.io/vue-gtag/). Go to Auto tracking for simplest way to add google analytics through this plugin.

- [free-for.dev](https://github.com/ripienaar/free-for-dev) resource to document the free alternatives to host a basic application/website.