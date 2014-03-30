from flask.ext.wtf import Form, RecaptchaField

from wtforms import TextField, BooleanField, TextAreaField, BooleanField, RadioField
from wtforms.validators import Required, Length, Email, EqualTo
from app.models import User

class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)


class OrderForm(Form):
    email = TextField('Enter your email:', validators = [Required(), Email(message=u'Invalid email address.')])
    email2 = TextField('Confirm your email:', validators = [EqualTo('email', message='Email address must match')])
    comments = TextAreaField('Anything else you need to tell us?')
    # captcha = RecaptchaField()
    order_type = RadioField('Select an order type', validators = [Required('Please select an order type')], 
                                                    choices=[('beta','I want to be a Beta Tester!'),
                                                             ('standard',"I'll wait until Beta Testing is finished. Put me on the Pre-Order List!")])


        
class PostForm(Form):
    post = TextField('post', validators = [Required()])
