from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, FormView

from apps.forms import StreamForm
from apps.models import Product, Category, WishList, Stream


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'apps/product/product-list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ProductMarketView(DetailView):
    model = Product
    template_name = 'apps/product/product-market.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        slug = self.request.GET.get('slug')
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        if slug:
            context['current_category'] = Category.objects.filter(slug=slug)
        return context

    def get_queryset(self):
        slug = self.request.GET.get('slug')
        qs = super().get_queryset()
        if slug:
            qs = qs.filter(category__slug=slug)
        return qs


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'apps/order/order.html'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        qs = self.get_queryset()
        pk = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)
        if pk:
            stream = get_object_or_404(Stream.objects.all(), pk=pk)
            stream.count += 1
            stream.save()
            return stream.product

        return get_object_or_404(Product.objects.all(), slug=slug)


class ProductListByCategoryView(ListView):
    queryset = Product.objects.all()
    template_name = 'apps/product/product-list.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        slug = self.kwargs.get('slug')
        if slug:
            queryset = queryset.filter(category__slug=slug)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ProductListByCategoryView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['current_category'] = self.kwargs.get('slug', 'all')
        return context


class ProductStatistView(DetailView):
    queryset = Product.objects.all()
    template_name = 'apps/product/product-status.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'product'


# class CategoryListView(ListView):
#     queryset = Category.objects.all()
#     template_name = 'apps/product/product-market.html'
#     context_object_name = 'categories'
#
#     def get_context_data(self, **kwargs):
#         context = super(CategoryListView, self).get_context_data(**kwargs)
#         context['products'] = Product.objects.all()
#         return context


class AddRemoveWishlistView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request, pk, *args, **kwargs):
        product = Product.objects.get(id=pk)
        obj = WishList.objects.filter(user=request.user, product=product)
        if obj.exists():
            obj.delete()
        else:
            WishList.objects.create(user=request.user, product=product)
        return redirect('product-list')


class WishlistView(LoginRequiredMixin, TemplateView):
    template_name = 'apps/wish-list.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        wishlists = WishList.objects.filter(user=self.request.user)
        context['wishlists'] = wishlists
        return context


class StreamFormView(FormView):
    form_class = StreamForm
    template_name = 'apps/thread.html'

    def form_valid(self, form):
        stream = form.save(False)
        stream.user = self.request.user
        stream.save()
        return redirect('product-list')
