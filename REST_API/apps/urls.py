from django.urls import path

from apps.views import CategoryListCreateAPIView, CategoryListView

urlpatterns = [
    # path('categories', CategoryListCreateAPIView.as_view(), name='category'),
    path('category', CategoryListView.as_view(), name='category'),
]