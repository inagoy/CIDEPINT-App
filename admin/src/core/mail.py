from flask import render_template
from flask_mail import Mail, Message

mail = Mail()


def init_app(app):
    mail.init_app(app)


def message(subject, recipients, template,
            sender="no-reply@cidepint.com", **kwargs):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.html = render_template(template, **kwargs)
    mail.send(msg)
