from django.contrib import admin
from django.contrib.admin import ModelAdmin, StackedInline, AdminSite

from apps.models import Category, Product, ProductImage, SiteSettings


@admin.register(Category)
class CategoryModelAdmin(ModelAdmin):
    exclude = 'slug', 'icon'


class ProductStackedInline(StackedInline):
    model = ProductImage


@admin.register(Product)
class ProductModelAdmin(ModelAdmin):
    inlines = ProductStackedInline,
    exclude = 'slug',


@admin.register(SiteSettings)
class SiteSettingsModelAdmin(ModelAdmin):

    # def has_add_permission(self, request):
    #     return False

    def has_delete_permission(self, request, obj=None):
        return False
