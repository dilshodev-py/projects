from django.apps import apps
from django.contrib import admin
from django.contrib.auth.models import Group, User
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from apps import models
from apps.models import Category

admin.site.unregister(Group)
admin.site.unregister(User)


class CustomDraggableMPTTAdmin(DraggableMPTTAdmin):
    # specify pixel amount for this ModelAdmin only:
    mptt_level_indent = 20


@admin.register(Category)
class CategoryAdmin(CustomDraggableMPTTAdmin):
    pass


