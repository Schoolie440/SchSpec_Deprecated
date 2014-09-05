import sys, os
virt_binary = "/home/schoolcr/testenv/bin/python"
if sys.executable != virt_binary: os.execl(virt_binary, virt_binary, *sys.argv)
sys.path.append(os.getcwd())

basedir = os.path.abspath(os.path.dirname(__file__))

if basedir == '/home/schoolcr/SchSpec':
  RUN_TYPE = 'production'
elif basedir == '/home/schoolcr/SchSpecTest':
  RUN_TYPE = 'test'
else:
  RUN_TYPE = 'local'

if RUN_TYPE == 'production':
  os.environ['SS_DATABASE_URL'] = 'mysql://schoolcr_SchSpec:specialties14@localhost/schoolcr_SchSpec'
elif RUN_TYPE == 'test':
  os.environ['SS_DATABASE_URL'] = 'mysql://schoolcr_SchSpec:specialties14@localhost/schoolcr_SchSpecTest'
else: 
  print 'Environment invalid'

from app import app as application