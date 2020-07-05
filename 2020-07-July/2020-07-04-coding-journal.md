[Checking postgres version](https://phoenixnap.com/kb/check-postgresql-version)

`locate bin/postgres` It will return the full path to our binary folder. Use this full path to display the current PostgreSQL version

`/usr/lib/postgresql/10/bin/postgres -V`

***

Upgrading Nuxt or other modules. [Resource](https://nuxtjs.org/guide/upgrading/)

1. Update the version specified for the nuxt package in your `package.json` file.
2. remove `package-lock.json` file
3. remove `node_modules` directory
4. Run the `npm install` command

***

WSGI path is being a pain in the ass.

`backendDev/backendDev/wsgi.py`
`backendDev/wsgi.py`
`backendDev.wsgi`
`backendDev.wsgi:application`

tried these all wsgi paths, none of them are working

***

`pip uninstall pkg-resource==0.0.0`

if `pkg-resource` package is in `requirements.txt`

NOTE: Apparently `pkg-resource` is necessary to run `eb create` so don't uninstall it rather remove it from `requirements.txt`

`pip install Django django-cors-headers djangorestframework djangorestframework_simplejwt psycopg2-binary awscli`