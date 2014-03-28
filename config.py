import os

basedir = os.path.abspath(os.path.dirname(__file__))

if basedir == '/home/apps/SchSpec':
  RUN_TYPE = 'production'
elif basedir == '/home/apps/SchSpecTest':
  RUN_TYPE = 'test'
else:
  RUN_TYPE = 'local'


CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]
    
if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')    

# email server
MAIL_SERVER='smtp.gmail.com'
MAIL_PORT=465
MAIL_USE_TLS = False
MAIL_USE_SSL= True
MAIL_USERNAME = 'brian.p.schoolcraft@gmail.com'
MAIL_PASSWORD = 'uuzjefbvsayddijh'


# administrator list
ADMINS = ['you@example.com']

# pagination
POSTS_PER_PAGE = 5
MAX_SEARCH_RESULTS = 50
