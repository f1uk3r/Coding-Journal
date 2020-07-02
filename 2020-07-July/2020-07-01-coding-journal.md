JS is not working in the version where I deployed my nuxt app in AWS Elastic Beastalk

Asked for help in discord and [stackoverflow](https://stackoverflow.com/questions/62671034/nuxtjs-app-deployed-to-elastic-beanstalk-javascript-not-working-in-the-deployed), no responses yet.

In the meanwhile I decided to try to make it work it in Amplify. I don't know exactly what is AWS Amplify but apparantly I can host my nuxt app on that, so should work for me

[Official docs for Amplify](https://docs.amplify.aws/cli/start/install)

## First try on Amplify

Following [this article](https://kodius.com/blog/nuxt-ssr-on-amplify/#setting-the-stage) to deploy nuxt app

First create a nuxt app

`npx create-nuxt-app <some-project>`

Configuring and Installing amplify, [watch this video](https://www.youtube.com/watch?v=fWbM5DLh25U) for reference

```
sudo npm install -g @aws-amplify/cli
amplify configure
amplify init
```

sudo is used here because without appropriate permission that command will result in an error

edit `/plugins/amplify.js` and `amplify/.config/project-config.json` as per the article

`amplify push`

had to delete the app. Article is asking to edit build command in the build setting to npm run generate. While it connected me to  the github repository, it errored out in building period of amplify app. Also there is no generate script in this nuxt 2.13.0. may use npm run build && npm run export