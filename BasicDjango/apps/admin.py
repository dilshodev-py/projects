from django.contrib import admin

from apps.models import Product, Category, Staff, Job, Organizer, Speaker, Room


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    pass
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass
@admin.register(Organizer)
class OrganizerAdmin(admin.ModelAdmin):
    pass
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass
@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    pass
