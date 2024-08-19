from apps.urls.auth import urlpatterns as auth_urls
from apps.urls.product import urlpatterns as product_urls

urlpatterns = auth_urls + product_urls