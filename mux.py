from hug_app.demo import __hug_wsgi__ as hug_app
from flask_app.demo import app as flask_app
from django_app.wsgi import application as django_app

import random


def app(environ, start_response):
    if environ['PATH_INFO'] == '/flask':
        environ['PATH_INFO'] = '/'
        return flask_app(environ, start_response)
    elif environ['PATH_INFO'] == '/hug':
        environ['PATH_INFO'] = '/'
        return hug_app(environ, start_response)
    elif environ['PATH_INFO'] == '/django':
        environ['PATH_INFO'] = '/'
        return django_app(environ, start_response)
    else:
        environ['PATH_INFO'] = '/'
        return random.choice((flask_app, django_app, hug_app))(environ, start_response)
