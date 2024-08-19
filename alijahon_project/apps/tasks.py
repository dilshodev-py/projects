from celery import shared_task
from django.core.mail import send_mail

from root.settings import EMAIL_HOST_USER


@shared_task
def add(receiver_email):
    subject = 'Djangochilar'
    message = 'xabar haqida'
    email_from = EMAIL_HOST_USER
    send_mail(subject, message, email_from, [receiver_email])

