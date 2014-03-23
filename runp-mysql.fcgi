#!flask/bin/python

use mysql
import os
if os.path.dirname(os.path.abspath(__file__)) == "SchSpec":
  os.environ['DATABASE_URL'] = 'mysql://apps:Amanda09@localhost/SchSpec'
elif os.path.dirname(os.path.abspath(__file__)) == "SchSpecTest":
  os.environ['DATABASE_URL'] = 'mysql://apps:Amanda09@localhost/SchSpecTest'

from flup.server.fcgi import WSGIServer
from app import app

if __name__ == '__main__':
    WSGIServer(app).run()