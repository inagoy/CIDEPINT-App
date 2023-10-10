from flask import render_template
from flask_mail import Mail, Message

mail = Mail()


def init_app(app):
    mail.init_app(app)


def message(subject, recipients, template,
            sender="no-reply@cidepint.com", **kwargs):
    """
    Send an email message using the provided subject, recipients, template,
    and optional sender.

    Args:
        subject (str): The subject of the email message.
        recipients (list): A list of email addresses to send the message to.
        template (str): The template to use for the email message.
        sender (str, optional): The email address of the sender.
        Defaults to "no-reply@cidepint.com".
        **kwargs: Additional keyword arguments to pass to the template.

    Returns:
        None
    """
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.html = render_template(template, **kwargs)
    mail.send(msg)
