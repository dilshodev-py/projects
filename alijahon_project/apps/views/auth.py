from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView

from apps.forms import UserModelForm
from apps.tasks import add


class ProfileView(LoginRequiredMixin, UpdateView):
    form_class = UserModelForm
    template_name = 'apps/auth/profile.html'
    login_url = reverse_lazy('login')
    success_url = 'profile'

    def get_object(self, queryset=None):
        return self.request.user


class CustomLoginView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'apps/auth/login.html')

    def post(self, *args, **kwargs):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user:
            login(self.request, user)
            return redirect('product-list')
        return redirect('login')

class SendView(View):
    def get(self, request, *args, **kwargs):
        email = request.GET.get('email')
        add.delay(email)
