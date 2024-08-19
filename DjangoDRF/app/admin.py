from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.contrib.auth.models import Group
from mptt.admin import DraggableMPTTAdmin
from app.models import Category, Product
from app.models import User

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)


@admin.register(Category)
class CategoryMPTTModelAdmin(DraggableMPTTAdmin):
    pass


@admin.register(Product)
class ProductModelAdmin(ModelAdmin):
    pass
