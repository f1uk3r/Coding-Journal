Lightsail

Resource: [Deploying to AWS LightSail - Django, Gunicorn, Nginx](https://www.nerdsgene.com/Article/DeployDjangoToLightSail)

Configuring components on ubuntu 16 to serve Django application using Gunicorn as our application server and Nginx as our reverse proxy server for serving client requests.

Amazon Lightsail derives its computing power from Elastic Compute Cloud (EC2). It is simpler to understand compute capacity that shares similar benefit as of EC2 but with restricted access.

Steps

1. [Creating Lightsail Instance.](https://lightsail.aws.amazon.com/ls/webapp/home/instances)

2. Download Private key from the instance just created and a .pem file should be downloaded.

3. Connecting to Lightsail using SSH

`sudo ssh –i <path to private key file> <username>@<public ip>`

`username` and `public ip` is displayed in the Lightsail instance on browser.

4. Installing `nginx python3-pip virtualenv` system wide in the Lightsail instance

```
sudo apt update
sudo apt install nginx python3-pip virtualenv
```

5. Setting up virtual environment

`virtualenv -p python3 djangoEnv`

6. Installing django and gunicorn in the virtualenv

```
source djangoEnv/bin/activate
pip3 install django gunicorn
cd djangoEnv
```

7. Setting up FileZilla

8. Uploading Local Project File

9. Setting Port 8000 Open in Lightsail. In Networking add a rule to Firewall 

`custom     TCP        8000`

10. Check Python Demo Server

`python manage.py runserver 0.0.0.0:8000`

11. setup postgresql on lightsail instance

12. Setting up Gunicorn

Checking Gunicorn

`file ../bin/gunicorn`

load the project's WSGI module using below command

`gunicorn --bind 0.0.0.0:8000 edhusk_django_api.wsgi:application`

13. If gunicorn works successfully, stop it with `ctrl+c` and deactivate our visual environment

`deactivate`

14. Creating Gunicorn Service File (See in the article)

If any modification is done to the gunicorn service file, reload the service daemon and restart gunicorn using below command

```
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
```

For checking status of gunicorn, run below command and below message should appear

```
sudo systemctl status gunicorn.socket
sudo systemctl status gunicorn
```

15. Setting up Nginx (See in the article)



***

# Gunicorn

## Resource: [What Is Gunicorn, and What Does It Do?](https://vsupalov.com/what-is-gunicorn/)

Three common building blocks when deploying a Python web application to production are :-

- A web server (like nginx)
- A WSGI application server (like Gunicorn)
- Actual application (written using frameworks like django)

the web server accepts requests, takes care of general domain logic and takes care of handling https connections. Only requests which are meant to arrice at the application are passed on toward the application server and the application itself. The application code does not care about anything except being able to process single requests.

## Gunicorn is a WSGI server. 

It is built so many different web servers can interact with it. It also does not really care what you used to build your web applicatiokn - as long as it can be interacted using the WSGI interface.

Gunicorn takes care of everything which happens in-between the web server and your web application. This way, when coding up your Django application you don't need to find your own solutions for:

- communicating with multiple web servers.
- reacting to lots of web requests at once and distributing the load 
- keeping multiple processes of the web application running.

## Web Server Gateway Interface (WSGI)

As described in [PEP3333](https://www.python.org/dev/peps/pep-3333/), the Python WSGI is a way to make sure that web servers and python web applications can talk to each other. To be more precise:

> The server side invokes a callable object that is provided by the application side.

So using a wsgi.py file, an object is defined which can be invoked by Gunicorn. This object is used to pass request data to your application, and to receive response data.

Gunicorn takes care of running multiple instances of your web application, making sureey are healthy and restart them as needed, distributing incoming requests across those instances and communicate with the web server.

If planning to run a Python web application in production, we'll want to make use of a WSGI server. This way our deployment will be more stable, be able to handle more requests at once and be fast about it. 

We can choose any WSGI servers we want and change the one using anytime we want without having to change our project in a big way.

***

nginx faile to create a symbolic link: file exists error

https://askubuntu.com/questions/543516/what-is-a-failed-to-create-a-symbolic-link-file-exists-error/

use `--force`