from django.contrib import admin
from django.urls import path, include

from apps.views import HomePageView, set_language

urlpatterns = [
    path('' , HomePageView.as_view(), name='home'),
    path('lang' , set_language, name='set_languagee'),
]