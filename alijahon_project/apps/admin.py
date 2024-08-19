from django.contrib import admin
from django.contrib.admin import ModelAdmin, StackedInline
from django.contrib.auth.models import Group
from django.utils.text import slugify

from apps.models import Product, Category, ProductImage
admin.site.unregister(Group)


@admin.register(Category)
class CategoryModelAdmin(ModelAdmin):
    fields = ['name', 'image']

    def save_form(self, request, form, change):
        slug = slugify(form.cleaned_data.get('name'))
        form.cleaned_data.update({'slug': slug})
        return form.save(commit=False)


class ProductStackedInline(StackedInline):
    model = ProductImage


@admin.register(Product)
class ProductModelAdmin(ModelAdmin):
    inlines = [ProductStackedInline]
    exclude = ('slug',)

    def save_form(self, request, form, change):
        slug = slugify(form.cleaned_data.get('name'))
        form.cleaned_data.update({'slug': slug})
        return form.save(commit=False)
