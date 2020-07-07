Title of the page and Meta tags

https://nuxtjs.org/api/pages-head/

```
data () {
  return {
    title: 'Hello World!'
  }
},
head () {
  return {
    title: this.title,
    meta: [
      // hid is used as unique identifier. Do not use `vmid` for it as it will not work
      { hid: 'description', name: 'description', content: 'My custom description' }
    ]
  }
}
  ```

***

favicon.ico in static folder have to be changed to change the website logo displayed in the search engines.

***

Integration of google analytics with Nuxtjs.

[Official google analytics module](https://github.com/nuxt-community/analytics-module)

`npm install --save-dev @nuxtjs/google-analytics`

in `nuxt.config.js`

```
export default {
  buildModules: [
    ['@nuxtjs/google-analytics', {
      id: 'UA-12301-2'
    }]
  ]
}
```

*** 

Vue/Nuxt `echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p` problem. [Resource](https://github.com/gatsbyjs/gatsby/issues/11406)

`echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p`

***

new environment for django app > edhusk-backend

***

Backend from scratch

`virtualenv -p /usr/bin/python edhusk-backend`

`source /home/f1uk3r/Coding/virtual-envs/edhusk-backend/bin/activate`

`python -m pip install Django`

`python -m django --version`

`django-admin startproject edhusk_django_api`

`sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib`

`sudo su - postgres`

`psql`

`CREATE DATABASE myproject;`

`CREATE USER myproject user WITH PASSWORD 'password';`

`ALTER ROLE myprojectuser SET client_encoding TO 'utf8';`

`ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';`

`ALTER ROLE myprojectuser SET timezone TO 'Asia/Kolkata';`

`GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;`

`pip install psycopg2-binary`

`\q`

`exit`

`git init`

`git add .`

`git commit -m "first commit"`

`git remote add origin https://github.com/f1uk3r/some-repository-name.git`

`git push -u origin master`

`pip install awsebcli`

`eb --version`

***

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html