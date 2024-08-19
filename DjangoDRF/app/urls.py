from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenVerifyView

from app.views import UserViewSet, CategoryListViewSet, ProductListViewSet, ProductDeleteViewSet, ProductCreateAPIView, \
     CategoryDeleteAPIView

router = DefaultRouter()

router.register('users', UserViewSet, basename='users')
# router.register('categories', CategoryListViewSet, basename='categories')
# router.register('products', ProductListViewSet, basename='products')

urlpatterns = [
    path('api/token/verify', TokenVerifyView.as_view(), name='token_verify'),

    path('categories', CategoryListViewSet.as_view(), name="category"),
    path('categories/<pk>', CategoryDeleteAPIView.as_view(), name="category"),

    path('products/create', ProductCreateAPIView.as_view(), name="product"),
    path('products/<pk>', ProductDeleteViewSet.as_view(), name="product"),
    path('products', ProductListViewSet.as_view(), name="product"),
]

# http://0.0.0.0:8001/swagger/
