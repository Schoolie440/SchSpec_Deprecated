from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, mail, db, lm
from forms import LoginForm, OrderForm
from models import User, ROLE_USER, ROLE_ADMIN, Order
from datetime import datetime
from config import POSTS_PER_PAGE, MAX_SEARCH_RESULTS
from sqlalchemy import desc

from flask.ext.mail import Message

from emails import order_confirmation



@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
@app.route('/Home', methods = ['GET', 'POST'])
def index():
  return render_template('index.html',
    title = 'Home')
    
@app.route('/SmartSwitch', methods = ['GET'])
@app.route('/smartswitch', methods = ['GET'])
def smartswitch():
  return render_template('smartswitch.html',
    title = 'The Smart Switch',
    description = " The Smart Switch mod for the Line 6 DL4. Finally, an easy way to tap in dotted 1/8ths on your Line 6 DL4. The DL4 Smart Switch gives you the ability to convert quarter notes to dotted eighth notes on any delay setting at any time. On top of that, you also get the option to switch quickly between two presets per delay type without the need of an external expression pedal.")
    
@app.route('/BenWrestling', methods = ['GET'])
def benwrestling():
  return render_template('benwrestling.html',
    title = "Ben's Wrestling")
	
@app.route('/about', methods = ['GET'])
def about():
  return render_template('about.html',
    title = 'About Us')
	
@app.route('/BarEnds', methods = ['GET'])
def barends():
  return render_template('barends.html',
    title = 'Heavy Stainless Bar Ends')
    
@app.route('/BarEnds/orders', methods = ['GET'])
def barend_orders():
  return render_template('barend_orders.html',
    title = 'Heavy Stainless Bar Ends')
    
@app.route("/sendemail")
def sendemail():
	msg = Message(
              'Hello',
	       sender='brian@schoolcraftspecialties.com',
	       recipients=
               ['brian.p.schoolcraft@gmail.com'])
	msg.body = "This is the email body"
	mail.send(msg)
	return "Sent"
  
@app.route("/orders")
@app.route("/orders/<int:page>")
@login_required
def orders(page = 1):
  orders = Order.query.order_by(desc(Order.id)).paginate(page, POSTS_PER_PAGE, False)
  return render_template('order_list.html',
    title = 'Admin - Orders',
    orders = orders)
    
@app.route("/smartswitch_order", methods = ['GET', 'POST'])
def smartswitch_order():
  form = OrderForm()
  if form.validate_on_submit():
    order = Order(email = form.email.data, 
            comments = form.comments.data,
            product = "SmartSwitch",
            order_date = datetime.utcnow(),
            order_type = 'smartswitch')
    db.session.add(order)
    db.session.commit()
    flash('Your order has been placed - Thank you!')
    order_confirmation(order)
    return redirect(url_for('smartswitch'))

  return render_template('smartswitch_order_form.html',
    title = 'Order Now - Smart Switch',
    form = form)
	
@lm.user_loader
def load_user(id):
    return User.query.get(int(id))
	
@app.route('/login', methods = ['GET', 'POST'])
# @lm.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        username = request.form['username']
        password = request.form['password']
        registered_user = User.query.filter_by(username=username).first()
        if registered_user:
          if registered_user.check_password(password):
            login_user(registered_user)
            flash('Logged in Successfully!')
            return redirect(request.args.get("next") or url_for("index"))
          else:
            flash('Invalid login. Please try again.')
            return redirect(url_for('login'))
        else:
          flash('Username not recognized. Please try again.')
          return redirect(url_for('login'))
          
        

    return render_template('login.html', 
        title = 'Sign In',
        form = form,
        providers = app.config['OPENID_PROVIDERS'])
		
# @oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email = resp.email).first()
    if user is None:
        return redirect(url_for('index'))
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))
	
@app.before_request
def before_request():
    g.user = current_user
	
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))