#!flask/bin/python

import os

basedir = os.path.abspath(os.path.dirname(__file__))

if basedir == '/home/apps/SchSpec':
  RUN_TYPE = 'production'
elif basedir == '/home/apps/SchSpecTest':
  RUN_TYPE = 'test'
else:
  RUN_TYPE = 'local'


if: RUN_TYPE == 'production':
  os.environ['SS_DATABASE_URL'] = 'mysql://apps:Amanda09@localhost/SchSpec'
elif RUN_TYPE == 'test':
  os.environ['SS_DATABASE_URL'] = 'mysql://apps:Amanda09@localhost/SchSpecTest'
else: 
  print 'Environment invalid'



from flup.server.fcgi import WSGIServer
from app import app

if __name__ == '__main__':
    WSGIServer(app).run()