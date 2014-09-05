from hashlib import md5
from app import db
from app import app
import re
from flask import url_for

from werkzeug.security import generate_password_hash, check_password_hash

ROLE_USER = 0
ROLE_ADMIN = 1


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True)
    pw_hash = db.Column(db.String(128))
    email = db.Column(db.String(120), unique = True)
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime)
    
    def __init__(self, username, password):
        self.username = username
        self.set_password(password)
        
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.username)
        
    def avatar(self, size):
        return 'http://www.gravatar.com/avatar/' + md5(self.email).hexdigest() + '?d=mm&s=' + str(size)
    @staticmethod
    def make_valid_nickname(nickname):
        return re.sub('[^a-zA-Z0-9_\.]', '', nickname)
        
    @staticmethod
    def make_unique_nickname(nickname):
        if User.query.filter_by(nickname = nickname).first() == None:
            return nickname
        version = 2
        while True:
            new_nickname = nickname + str(version)
            if User.query.filter_by(nickname = new_nickname).first() == None:
                break
            version += 1
        return new_nickname

class Order(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(140))
    product = db.Column(db.String(20))
    options = db.Column(db.String(140))
    order_date = db.Column(db.DateTime)
    order_type = db.Column(db.String(20))
    paid = db.Column(db.Boolean) 
    paid_date = db.Column(db.DateTime)
    shipped = db.Column(db.Boolean)
    shipped_date = db.Column(db.DateTime)
    tracking = db.Column(db.String(80))
    address1 = db.Column(db.String(80))
    address2 = db.Column(db.String(80))
    city = db.Column(db.String(80))
    state = db.Column(db.String(80))
    postalCode = db.Column(db.String(80))
    country = db.Column(db.String(80))
    comments = db.Column(db.String(500))


    def __repr__(self):
        return '<Order %r, %r>' % (self.id, self.product)
        

        