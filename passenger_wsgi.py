import sys, os

basedir = os.path.abspath(os.path.dirname(__file__))

if basedir == '/home/schoolcr/SchSpec':
  RUN_TYPE = 'production'
elif basedir == '/home/schoolcr/SchSpecTest':
  RUN_TYPE = 'test'
else:
  RUN_TYPE = 'local'
  




if RUN_TYPE == 'production':
  os.environ['SS_DATABASE_URL'] = 'mysql://schoolcr_SchSpec:specialties14@localhost/schoolcr_SchSpec'
  virt_binary = "/home/schoolcr/pyenv/bin/python"

elif RUN_TYPE == 'test':
  os.environ['SS_DATABASE_URL'] = 'mysql://schoolcr_SchSpec:specialties14@localhost/schoolcr_SchSpecTest'
  virt_binary = "/home/schoolcr/testenv/bin/python"

else: 
  print 'Environment invalid'
  
if sys.executable != virt_binary: os.execl(virt_binary, virt_binary, *sys.argv)
sys.path.append(os.getcwd())

from app import app as application
