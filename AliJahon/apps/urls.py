from django.contrib.auth.views import LogoutView
from django.urls import path

from apps.views import CategoryListView, \
    OrderSuccessTemplateView, OrderListView, LikeProductView, MyWishListView, MainModelListView, \
    CustomLoginFormView, ProfileUpdateView, MarketListView, StreamFormView, StreamListView, StatisticsListView, \
    StreamDetailView, OperatorListView, get_districts_by_region, RequestTemplateView, ProductFormView

urlpatterns = [
    path('', MainModelListView.as_view(), name='main'),
    path('category/trade', CategoryListView.as_view(), name='category_trade'),
    path('oqim/<int:pk>', StreamDetailView.as_view(), name='oqim'),

]

urlpatterns += [
    path('product/<str:slug>', ProductFormView.as_view(), name='product_detail'),
    path('product/wishlist/<str:slug>', LikeProductView.as_view(), name='wishlist'),
    path('my-product/wishlist', MyWishListView.as_view(), name='my_wishlist'),
]

urlpatterns += [
    # path('order/create', OrderFormView.as_view(), name='order_create'),
    path('order/list', OrderListView.as_view(), name='order_list'),
    path('order/success', OrderSuccessTemplateView.as_view(), name='order_success')
]

urlpatterns += [
    path('admin_page/market', MarketListView.as_view(), name='market'),
    path('admin_page/stream-form', StreamFormView.as_view(), name='stream_form'),
    path('admin_page/stream/list', StreamListView.as_view(), name='stream_list'),
    path('admin_page/stats', StatisticsListView.as_view(), name='admin_statistic'),
    path('admin_page/request', RequestTemplateView.as_view(), name='request')
]

urlpatterns += [
    path('operator', OperatorListView.as_view(), name='operator'),
    path('operator/ajax/get-districts/<int:region_id>/', get_districts_by_region, name='get_districts_by_region'),
]

urlpatterns += [
    path('auth/logout', LogoutView.as_view(template_name='apps/auth/login.html'), name='logout'),
    path('auth/login', CustomLoginFormView.as_view(), name='login'),
    path('auth/profile', ProfileUpdateView.as_view(), name='profile')
]
