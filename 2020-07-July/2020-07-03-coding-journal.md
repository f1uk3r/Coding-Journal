removed that extend function in the build in nuxt.config.js. Pushed it to github and deployed with aws amplify

And it actually worked. i don't know what that extend function was doing to break the build but removing it did solved my problem

now there is some problem with dynamic route. I do remember an article I read which talked exclusively about dynamic route in Amplify tutorial. This should be a known problem

Pretty easy, found the [article](https://medium.com/@pascalluther/deploy-a-nuxt-spa-app-to-amazons-aws-amplify-74994d4326c1) on first go. See the `3) Fix the app to work with dynamic routes`. Worked flawlessly for me

***

## Deployment for django

Apparantly AWS now launched a service `Lightsail` which gives out of the box deployment for Django.

For now, I'll focus on elastic beanstalk

This is a very good [article](https://realpython.com/deploying-a-django-app-and-postgresql-to-aws-elastic-beanstalk/) about deploying a django project on elastic beanstalk. Almost every time I have deployed the project, this article have helped me. Here are the [official docs](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html) on how to deploy django project on elastic beanstalk.

Install `awsebcli` which basically provide us shell commands to deploy on Elastic Beanstalk

`pip install awsebcli`

Check cli version with

`eb --version`

Now configure EB cli

`eb init`

Ater initialising eb on the project we can use `eb console` to open and navigate Elastic Beanstalk console in the default browser.

Now to make an environment in the Elastic Beanstalk console, we can use the following command

`eb create`

On environment creation it error out with `ERROR   Your requirements.txt is invalid. Snapshot your logs for details.` I searched for the error and got this [stackoverflow question](https://stackoverflow.com/questions/18554666/invalid-requirements-txt-on-deploying-django-app-to-aws-beanstalk) basically saying the same thing. In answer someone talked about adding `postgresql93-devel` in `.ebextensions`. In our earlier project I have a file doing just that so I hope that the `realpython` article might have answer to it.

Yeah they addressed this error in the article, so we should be fine.

`eb logs` for logs

Read the fucking logs. So even if they addressed the issue in the article there was an another problem in the requirements.txt in my case. I have a packge `pkg-resource==0` and there is no package with this name. I have to do `pip uninstall pkg-resource==0.0.0`. [Resource](https://stackoverflow.com/questions/40670602/could-not-find-a-version-that-satisfies-the-requirement-pkg-resources-0-0-0)

In the article we are provided with 2 ways to setup our wsgi path, I will be doing the 2nd way because I don't know where wsgi path is in our Elastic Beanstalk environment

Will continue tomorrow

***
## Misc

[Stackshare](https://stackshare.io/): looks like a cool website for knowing the stack different companies are using.

Tawk.to and nuxt integration. [Resource](https://stackoverflow.com/questions/51644901/using-tawk-to-with-nuxt-vue-application)