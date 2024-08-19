from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import Task, Vacancy, Company

# Register your models here.
admin.site.register(Company)
admin.site.register(Vacancy)
@admin.register(Task)
class TaskAdmin(ModelAdmin):
    pass

