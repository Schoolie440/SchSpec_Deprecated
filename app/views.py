from flask import render_template, flash, redirect, session, url_for, request, g
# from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, mail, db #, lm, oid
from forms import LoginForm, OrderForm
from models import User, ROLE_USER, ROLE_ADMIN, Order
from datetime import datetime
from config import POSTS_PER_PAGE, MAX_SEARCH_RESULTS
from sqlalchemy import desc

from flask.ext.mail import Mail, Message


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

@app.route('/joetest', methods = ['GET'])
def joetest():
  return render_template('joetest.html',
    title = 'Testing, 1, 2, 3')

@app.route('/briantest', methods = ['GET'])
def briantest():
  return render_template('briantest.html',
    title = 'Testing, 1, 2, 3')
	
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
	       sender='me@example.com',
	       recipients=
               ['brian.p.schoolcraft@gmail.com'])
	msg.body = "This is the email body"
	mail.send(msg)
	return "Sent"
  
@app.route("/orders")
@app.route("/orders/<int:page>")
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
            order_type = form.order_type.data)
    db.session.add(order)
    db.session.commit()
    # flash('Your order has been placed - Thank you!')
    return redirect(url_for('smartswitch'))

  return render_template('smartswitch_order_form.html',
    title = 'Order Now - Smart Switch',
    form = form)