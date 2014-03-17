from flask.ext.wtf import Form, RecaptchaField

from wtforms import TextField, BooleanField, TextAreaField, BooleanField, RadioField
from wtforms.validators import Required, Length, Email, EqualTo

class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)

from app.models import User

class OrderForm(Form):
    email = TextField('Enter your email:', validators = [Required(), Email(message=u'Invalid email address.'), EqualTo('email2', message='Email address must match')])
    email2 = TextField('Confirm your email:')
    beta = BooleanField('beta')
    comments = TextAreaField('Anything else you need to tell us?')
    captcha = RecaptchaField()
    order_type = RadioField('Label', choices=[('beta','I want to be a Beta Tester!'),
                                              ('standard',"I'll wait until Beta Testing is finished. Put me on the Pre-Order List!")])


        
class PostForm(Form):
    post = TextField('post', validators = [Required()])
