from django.core.mail import send_mail
from django.conf import settings

def send_email(form_data):
    subject = "New Contact Message"
    name = form_data.get("name")
    email = form_data.get("email")
    message = form_data.get("message")

    message = f"""
        Name: {name}
        Email: {email}
        Message: {message}
    """
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [settings.EMAIL_HOST_USER]

    send_mail(subject, message, from_email, recipient_list)