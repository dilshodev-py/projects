from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include

from apps.views import HomeTemplateView, SendEmailView, RegisterFormView, verify_email, verify_email_confirm

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='index'),
    path('login', LoginView.as_view(template_name='apps/auth/login.html'), name='login'),
    path('register', RegisterFormView.as_view(), name='register'),
    path('verify-email/', verify_email, name='verify-email'),
    path('verify-email-confirm/<uidb64>/<token>/', verify_email_confirm, name='verify-email-confirm'),
]
