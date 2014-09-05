from flask import render_template
from config import ADMINS
from flask.ext.mail import Message
from app import mail
from decorators import async

@async
def send_async_email(msg):
    mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender = sender, recipients = recipients)
    msg.body = text_body
    msg.html = html_body
    send_async_email(msg)


def order_confirmation(order):
    send_email("Order Confirmation - Schoolcraft Specialties",
        ADMINS[0],
        [order.email],
        render_template("email_order_response.txt"),
        render_template("email_order_response.html"))
    send_email("Order Notification - Schoolcraft Specialties",
        ADMINS[0],
        ['brian@schoolcraftspecialties.com'],
         # 'joe@schoolcraftspecialties.com'],
        render_template("email_order_notification.txt", order = order),
        render_template("email_order_notification.html", order = order))