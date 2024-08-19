import re
from datetime import timedelta, datetime

from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Q, F, Sum
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, TemplateView, DetailView, UpdateView, FormView

from apps.filters import OrderFilterSet
from apps.forms import UserModelForm, OrderModelForm, LoginForm, RegisterForm, StreamForm
from apps.models import Category, Product, Order, User, WishList, Stream, Region, District, SiteSettings


class MainModelListView(ListView):
    model = Product
    template_name = 'apps/trade/main.html'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        return context


class CategoryListView(ListView):
    model = Product
    template_name = 'apps/trade/category.html'
    context_object_name = 'products'
    paginate_by = 1

    def get_queryset(self):
        slug = self.request.GET.get('slug')
        query = super().get_queryset()
        if slug:
            query = query.filter(category__slug=slug)
        return query

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        if slug := self.request.GET.get('slug'):
            context['slug'] = slug
        return context


class CustomRegisterFormView(FormView):
    form_class = RegisterForm
    template_name = 'apps/auth/register.html'

    def form_valid(self, form):
        first_name = form.data.get('first_name')
        phone_number = form.data.get('phone_number')
        password = form.data.get('password')
        User.objects.get_or_create(first_name=first_name, phone_number=phone_number, password=password)
        return redirect('login')


class CustomLoginFormView(FormView):
    form_class = LoginForm
    template_name = 'apps/auth/login.html'

    def form_valid(self, form):
        phone_number = re.sub(r'\D', '', form.data.get('phone_number'))
        password = form.data.get('password')

        user, created = User.objects.get_or_create(phone_number=phone_number)

        if created:
            user.set_password(password)
            user.save()

        user = authenticate(self.request, phone_number=phone_number, password=password)
        if user or created:
            login(self.request, user)
            roles = {
                User.Role.USER: 'main',
                User.Role.OPERATOR: 'operator'
            }
            return redirect(roles.get(user.role))
        messages.success(self.request, 'Your form invalid')
        return redirect('login')


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserModelForm
    template_name = 'apps/auth/profile.html'
    success_url = 'profile'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['regions'] = Region.objects.all()
        if region_id := self.request.user.region:
            context['districts'] = District.objects.filter(region_id=region_id)
        return context


class MyWishListView(LoginRequiredMixin, ListView):
    queryset = WishList.objects.select_related('product')
    template_name = 'apps/wish-list.html'
    paginate_by = 6


class LikeProductView(View):
    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, slug=kwargs.get('slug'))
        obj, created = WishList.objects.get_or_create(user=request.user, product=product)
        if not created:
            obj.delete()
            return JsonResponse({'save': 0})
        return JsonResponse({'save': 1})


class OrderSuccessTemplateView(TemplateView):
    template_name = 'apps/trade/order-success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['delivery_price'] = SiteSettings.objects.first().delivery_price
        return context


class OrderListView(ListView):
    queryset = Order.objects.all()
    template_name = 'apps/trade/order-list.html'
    paginate_by = 5

    def get_queryset(self):
        query = super().get_queryset().filter(user=self.request.user).select_related('product')
        return query.values('product__name', 'amount_price', 'status', 'created_at')


class ProductFormView(FormView, DetailView):
    model = Product
    form_class = OrderModelForm
    template_name = 'apps/trade/product-detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['delivery_price'] = SiteSettings.objects.all().first().delivery_price
        return context

    def form_valid(self, form):
        form = form.save(commit=False)
        form.user = self.request.user
        self.object = form.product
        form.amount_price = form.product.price + self.get_context_data().get('delivery_price')
        form.save()
        return render(self.request, template_name='apps/trade/order-success.html', context=self.get_context_data())






class MarketListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'apps/market/product-market.html'
    paginate_by = 1

    def get_queryset(self):
        slug = self.request.GET.get('slug')
        query = super().get_queryset()
        if slug:
            query = query.filter(category__slug=slug)
        return query

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['categories'] = Category.objects.all()
        return context


class StreamFormView(FormView):
    form_class = StreamForm
    template_name = 'apps/market/stream-list.html'

    def form_valid(self, form):
        stream = form.save(False)
        stream.user = self.request.user
        stream.save()
        return redirect('stream_list')


class StreamDetailView(DetailView):
    queryset = Stream.objects.select_related('product').all()
    template_name = 'apps/trade/product-detail.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        Stream.objects.filter(id=obj.id).update(count=F('count') + 1)
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = context.get('product').product
        context['delivery_price'] = SiteSettings.objects.first().delivery_price
        return context


class StreamListView(LoginRequiredMixin, ListView):
    queryset = Stream.objects.all()
    template_name = 'apps/market/stream-list.html'
    paginate_by = 6

    def get_queryset(self):
        query = super().get_queryset().filter(user=self.request.user)
        query = query.select_related('product').values('id', 'name', 'count', 'product__slug')
        return query


class StatisticsListView(ListView):
    queryset = Stream.objects.all()
    template_name = 'apps/market/statistic-stream.html'
    context_object_name = 'streams'

    def time_filter(self, qs):
        period = self.request.GET.get('period')
        today = datetime.now().date()
        start_date = None
        time_between = {
            "today": (today, today),
            "last_day": (today - timedelta(days=1), start_date),
            "wekly": (today - timedelta(days=today.weekday()), today),
            "monthly": (
                today.replace(day=1), (today.replace(day=28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)),
        }
        time_filter_option = {}
        if period:
            time_filter_option = {"created_at__date__range": time_between.get(period)}
        return qs.filter(**time_filter_option, user=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        qs = self.get_queryset()
        context = super().get_context_data(object_list=object_list, **kwargs)

        context.update(**qs.aggregate(
            total_NEW=Sum('new_count'),
            total_READY_TO_START=Sum('ready_to_start_count'),
            total_BEING_DELIVERED=Sum('being_delivered_count'),
            total_DELIVERED=Sum('delivered_count'),
            total_NOT_PICK_UP_PHONE=Sum('not_pick_up_phone_count'),
            total_CANCELED=Sum('canceled_count'),
            total_ARCHIVED=Sum('archived_count'),
            total_COUNT=Sum('count')
        ))
        return context

    def get_queryset(self):
        qs = super().get_queryset().filter(user=self.request.user).select_related('product').annotate(
            new_count=Count('orders', filter=Q(orders__status=Order.Status.NEW)),
            ready_to_start_count=Count('orders', filter=Q(orders__status=Order.Status.READY_TO_START)),
            being_delivered_count=Count('orders', filter=Q(orders__status=Order.Status.BEING_DELIVERED)),
            delivered_count=Count('orders', filter=Q(orders__status=Order.Status.DELIVERED)),
            not_pick_up_phone_count=Count('orders', filter=Q(orders__status=Order.Status.NOT_PICK_UP_PHONE)),
            canceled_count=Count('orders', filter=Q(orders__status=Order.Status.CANCELED)),
            archived_count=Count('orders', filter=Q(orders__status=Order.Status.ARCHIVED))
        ).values('name', 'product__name', 'count', 'new_count', 'ready_to_start_count', 'being_delivered_count',
                 'delivered_count', 'not_pick_up_phone_count', 'canceled_count', 'archived_count')
        return self.time_filter(qs)


class OperatorListView(ListView):
    queryset = Order.objects.all()
    template_name = 'apps/operator/operator-page.html'
    success_url = reverse_lazy('operator')
    context_object_name = 'orders'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['regions'] = Region.objects.all()
        context['districts'] = District.objects.all()
        context['categories'] = Category.objects.all()
        context['orders'] = OrderFilterSet(self.request.GET, queryset=Order.objects.all())  # TODO class attr otkazish
        return context


class RequestTemplateView(TemplateView):  # TODO ListView
    template_name = 'apps/request.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['requests'] = Order.objects.filter(
            stream__user=self.request.user).select_related('product', 'stream', 'district')

        return data


def get_districts_by_region(request, region_id):
    districts = District.objects.filter(region_id=region_id).values('id', 'name')
    return JsonResponse(list(districts), safe=False)
