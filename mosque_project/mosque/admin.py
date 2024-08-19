from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.db.models import Sum, F, Count
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
import pandas as pd
from openpyxl.styles import Alignment

from apps.fixtures.main import moliya_header
from mosque.filters import CustomDateRangeFilter
from apps.models import User, UserRole
from apps.models import UserStaffProxy
from mosque.models import Mosque, Transaction, TransactionType
from xlsxdocument import XLSXDocument, export_selected

from root.settings import BASE_DIR

admin.site.unregister(Group)


@admin.register(UserRole)
class UserRoleModelAdmin(ModelAdmin):
    pass


@admin.register(UserStaffProxy)
class UserStaffProxyModelAdmin(UserAdmin):
    list_filter = []
    search_fields = "username", "first_name", "last_name"
    list_display = "username", "first_name", "last_name", "is_staff"
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "birthday", "mosque", "role", "salary")}),
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


@admin.register(Mosque)
class MosqueModelAdmin(ModelAdmin):
    actions = ['export_to_excel']
    list_filter = ["name", ('created_at', CustomDateRangeFilter)]
    list_display = 'name', 'account_number', 'staff_count', 'income', 'expenses'
    fieldsets = (
        ("Masjid malumotlari", {"fields": ("name", "address",)}),
        ("Bank malumotlari", {"fields": ("account_number", "bank", "bank_code", "stir")}),
    )
    filter_horizontal = []

    def export_to_excel(self, request, queryset):
        df = pd.DataFrame(list(
            queryset.prefetch_related('users').annotate(masjid_nomi=F('name'), hodimlar_soni=Count('users')).values(
                'masjid_nomi', 'hodimlar_soni')))
        df.index += 1
        df.index.name = '№'
        file_path = f"{BASE_DIR}/excel_file.xlsx"
        types = list(TransactionType.objects.filter(income=True).values_list('name', flat=True))
        df_additional = pd.DataFrame(columns=moliya_header() + types)
        df = pd.concat([df, df_additional], axis=1)
        with pd.ExcelWriter(file_path) as writer:
            df.to_excel(writer, sheet_name='moliya hisobot', startrow=3)
            worksheet = writer.sheets['moliya hisobot']
            for col in worksheet.columns:
                max_length = 0
                for cell in col:
                    if cell.row == 4:  # Header row
                        max_length = max(max_length, len(str(cell.value)))
                adjusted_width = (max_length + 10) * 1.2
                worksheet.column_dimensions[col[0].column_letter].width = adjusted_width
            adjusted_height = (max_length + 30) * 1.2  # Adjust the multiplier (1.2) as needed
            worksheet.row_dimensions[4].height = adjusted_height
            for col in worksheet.iter_cols():
                for cell in col:
                    cell.alignment = Alignment(horizontal='center', vertical='center')
        self.message_user(request, f"Data exported to Excel file: {file_path}")
        with open(file_path, 'rb') as excel_file:
            response = HttpResponse(excel_file.read(),
                                    content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=exported_data.xlsx'
        return response

    export_to_excel.short_description = "Export selected items to Excel"

    @admin.display(description='Hodimlar soni')
    def staff_count(self, obj):
        return obj.users.count()

    @admin.display(description='Xarajati')
    def expenses(self, obj):
        return obj.transactions.filter(mosque__id=obj.id, type__income=False).aggregate(
            total_amount=Sum('amount'))['total_amount']

    @admin.display(description='Daromadi')
    def income(self, obj):
        return obj.transactions.filter(mosque__id=obj.id, type__income=True).aggregate(
            total_amount=Sum('amount'))['total_amount']


@admin.register(Transaction)
class TransactionModelAdmin(ModelAdmin):
    pass


@admin.register(TransactionType)
class TransactionTypeModelAdmin(ModelAdmin):
    list_display = 'name', 'income'
    search_fields = 'income',
