from django.urls import path

from apps.views import ProductDetailView, ProductListView

# from apps.views import product_list_view, product_detail_view, product_list2_view

urlpatterns = [
    path('product-list', ProductListView.as_view() , name = 'product_list'),
    path('product-detail/<int:pk>', ProductDetailView.as_view() , name = 'product_detail'),
    # path('product-list2', product_list2_view , name = 'product_list2'),
]

