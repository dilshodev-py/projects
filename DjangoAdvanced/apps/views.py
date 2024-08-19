from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views.generic import DetailView, ListView

from apps.models import Product, Category


#
# def product_list_view(request):
#     products = Product.objects.all()
#     category_id = request.GET.get("category_id")
#     if category_id:
#         products = products.filter(category_id=category_id)
#     context = {
#         "categories": Category.objects.all(),
#         "products": products,
#     }
#     return TemplateResponse(request, 'apps/product-list.html', context=context)
#
#
# def product_list2_view(request):
#     context = {
#         "categories": Category.objects.all(),
#     }
#     return TemplateResponse(request, 'apps/product-list2.html', context=context)
#
#
# def product_detail_view(request, pk: int):
#     product = Product.objects.filter(pk=pk).first()
#     return TemplateResponse(request, 'apps/product-detail.html', {"product": product})


class ProductListView(ListView):
    queryset = Category.objects.all()
    context_object_name = "categories"
    template_name = 'apps/product-list.html'

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        category_id = self.request.GET.get("category_id")
        data['products'] = Product.objects.all()
        if category_id:
            data['products'] = data.get("products").filter(category_id=category_id)
        return data


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'apps/product-detail.html'
