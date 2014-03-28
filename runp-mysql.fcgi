#!flask/bin/python

import os
from config import RUN_TYPE

if RUN_TYPE == 'production':
  os.environ['DATABASE_URL'] = 'mysql://apps:Amanda09@localhost/SchSpec'
elif RUN_TYPE == 'test':
  os.environ['DATABASE_URL'] = 'mysql://apps:Amanda09@localhost/SchSpecTest'

from flup.server.fcgi import WSGIServer
from app import app

if __name__ == '__main__':
    WSGIServer(app).run()