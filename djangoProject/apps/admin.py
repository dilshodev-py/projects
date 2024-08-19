from django.contrib import admin
from django.contrib.admin import ModelAdmin, StackedInline
from django.contrib.contenttypes.models import ContentType
from mptt.admin import MPTTModelAdmin

from apps.models import Category, Product, ProductImage, User


class CustomMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20


admin.site.register(Category, CustomMPTTModelAdmin)


class ProductStackedInline(StackedInline):
    model = ProductImage


@admin.register(Product)
class CategoryModelAdmin(ModelAdmin):
    inlines = [ProductStackedInline]

@admin.register(User)
class UserModelAdmin(ModelAdmin):
    pass


