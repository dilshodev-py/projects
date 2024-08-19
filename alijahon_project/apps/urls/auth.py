from django.contrib.auth.views import LogoutView
from django.urls import path

from apps.views import CustomLoginView, ProfileView, SendView

urlpatterns = [
    path('login', CustomLoginView.as_view(), name='login'),
    # path('register', RegisterView.as_view(), name='register'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('logout', LogoutView.as_view(next_page='product-list'), name='logout'),
    path('send', SendView.as_view()),
]
