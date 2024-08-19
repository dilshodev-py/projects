from django.urls import path

from apps.views import ProductListView, ProductDetailView, ProductListByCategoryView, \
    WishlistView, AddRemoveWishlistView
from apps.views import StreamFormView
from apps.views.order import StatisticListView
from apps.views.product import ProductStatistView, ProductMarketView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product/detail/<str:slug>', ProductDetailView.as_view(), name='product_detail'),
    path('product/oqim/<int:pk>', ProductDetailView.as_view(), name='order_stream_page'),
    path('product/statist/<str:slug>', ProductStatistView.as_view(), name='product_statist'),
    path('product/market', ProductMarketView.as_view(), name='market_by_category'), # TODO query param
    # path('product/market/<str:slug>', ProductMarketView.as_view(), name='market-by-category'),


    path('product/stream', StreamFormView.as_view(), name='stream'),
    path('stream/statistika', StatisticListView.as_view(), name='stream_statistika'),
    path('category/<str:slug>', ProductListByCategoryView.as_view(), name='product_list_by_category'),
    path('category', ProductListByCategoryView.as_view(), name='product_all_list_by_category'),

    path('wishlist', WishlistView.as_view(), name='wishlist'),
    path('wishlist/<int:pk>', AddRemoveWishlistView.as_view(), name='add_remove_wishlist'),
]

