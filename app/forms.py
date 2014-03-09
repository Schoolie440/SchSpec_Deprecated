from flask.ext.wtf import Form
#from flask.ext.wtf import Form, TextField, BooleanField, TextAreaField
#from flask.ext.wtf import Required, Length

from wtforms import TextField, BooleanField, TextAreaField
from wtforms.validators import Required, Length, Email

class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)

from app.models import User

class OrderForm(Form):
    email = TextField('email', validators = [Required(), Email(message=u'Invalid email address.')])
    comments = TextAreaField('comments')

        
class PostForm(Form):
    post = TextField('post', validators = [Required()])
