from django.contrib import admin
from django.contrib.auth.models import User, Group

from apps.models import Category, Product

admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
