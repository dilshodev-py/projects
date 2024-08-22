from django.conf.urls.i18n import i18n_patterns
from django.urls import path

from apps.views import HomePage, set_language_view

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('setlanguage', set_language_view, name='set_language'),

]


