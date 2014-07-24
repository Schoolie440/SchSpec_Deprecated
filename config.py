import os

basedir = os.path.abspath(os.path.dirname(__file__))

if basedir == '/home/apps/SchSpec':
  RUN_TYPE = 'production'
elif basedir == '/home/apps/SchSpecTest':
  RUN_TYPE = 'test'
else:
  RUN_TYPE = 'local'
  
print '\n\nEnvironment: ' + RUN_TYPE + '\n\n'


CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]
    
    
if RUN_TYPE == 'test':
  if os.environ.get('SS_DATABASE_URL') is None:
    print 'DB Error - No Environment Variable'
    DB_STATUS = 'Env: Test; No Environment Variable'
  else:
    SQLALCHEMY_DATABASE_URI = os.environ['SS_DATABASE_URL']
    DB_STATUS = 'Env: Test'
elif RUN_TYPE == 'production':
  if os.environ.get('SS_DATABASE_URL') is None:
    print 'DB Error - No Environment Variable'
    DB_STATUS = 'Env: production; No Environment Variable'    
  else:
    SQLALCHEMY_DATABASE_URI = os.environ['SS_DATABASE_URL']
    DB_STATUS = 'Env: Production'

elif RUN_TYPE == 'local':
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    DB_STATUS = 'Env: Local'
else: 
  print 'Environment invalid'
  DB_STATUS = 'Env: Invalid'


SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')    

# email server
MAIL_SERVER='in.mailjet.com'
MAIL_PORT=465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = '40b18d21fface7a358c736e6a805d7d9'
MAIL_PASSWORD = '974c434062267b6f886fe8da8a764030'


# administrator list
ADMINS = ['admin@schoolcraftspecialties.com',
          'brian@schoolcraftspecialties.com']

# pagination
POSTS_PER_PAGE = 5
MAX_SEARCH_RESULTS = 50
