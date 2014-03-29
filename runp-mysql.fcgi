#!flask/bin/python

import os

basedir = os.path.abspath(os.path.dirname(__file__))

if basedir == '/home/apps/SchSpec':
  os.environ['DATABASE_URL'] = 'mysql://apps:Amanda09@localhost/SchSpec'
elif basedir == '/home/apps/SchSpecTest':
  os.environ['DATABASE_URL'] = 'mysql://apps:Amanda09@localhost/SchSpecTest'

from flup.server.fcgi import WSGIServer
from app import app

if __name__ == '__main__':
    WSGIServer(app).run()