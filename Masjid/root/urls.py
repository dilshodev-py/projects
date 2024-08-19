from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from root import settings

urlpatterns = [
    path('', admin.site.urls),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
