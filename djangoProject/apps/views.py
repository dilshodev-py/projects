from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, UpdateView, FormView

from apps.forms import UserModelForm
from apps.mixins import NotLoginRequiredMixin
from apps.models import Product, Category, User


class ProductListView(ListView):
    queryset = Product.objects.all()
    context_object_name = 'products'
    template_name = 'product-list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['categories'] = Category.objects.all()
        return context


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    context_object_name = 'product'
    pk_url_kwarg = 'pk'
    template_name = 'product-detail.html'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'
    login_url = reverse_lazy('product-list')


class ProfileUpdateView(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'phone_number', 'email', 'photo']
    success_url = '/profile'

# class CustomLoginView(NotLoginRequiredMixin, View):
#     def get(self, *args, **kwargs):
#         return render(self.request, 'apps/auth/index.html')
#
#     def post(self, *args, **kwargs):
#         username = self.request.POST.get('username')
#         password = self.request.POST.get('password')
#         user = authenticate(self.request, username=username, password=password)
#         if user:
#             login(self.request, user)
#             return redirect('product-list')
#         return redirect('custom_login_view')

class ProfileFormView(LoginRequiredMixin, UpdateView):
    form_class = UserModelForm
    success_url = reverse_lazy('profile')
    template_name = 'profile.html'
    login_url = reverse_lazy('product-list')

    def get_object(self, queryset=None):
        return self.request.user




