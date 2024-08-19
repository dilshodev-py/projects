from time import time

from celery import shared_task
from django.core.mail import send_mail

from root import settings


@shared_task
def send_to_email(subject , receiver_email , msg):

    start = time()
    send_mail(subject , msg , settings.EMAIL_HOST_USER , [receiver_email] )
    end = time()
    return {"status" : "Yuborildi" , "time" : int(end-start) , "email" : receiver_email}



