from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from apps.models import User


@admin.register(User)
class UserModelAdmin(UserAdmin):
    search_fields = ("username", "first_name", "last_name")
    list_display = "username", "first_name", "last_name", "is_staff"
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "birthday","passport_number" , "command_file","salary", "mosque", "role")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "groups",
                    "user_permissions",
                ),
            },
        )
    )

    def get_queryset(self, request):
        return super().get_queryset(request).filter(type=User.Type.STAFF)

