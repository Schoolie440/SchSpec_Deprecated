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


def order_confirmation(email):
    send_email("Order Confirmation - Schoolcraft Specialties",
        ADMINS[0],
        [email],
        render_template("email_order_response.txt"),
        render_template("email_order_response.html"))