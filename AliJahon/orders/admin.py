from django.contrib import admin
from django.contrib.admin import ModelAdmin
from orders.models import NewOrder, ReadyToStartOrder, BeingDeliveredOrder, NotPickUpPhoneOrder, CanceledOrder, \
    ArchivedOrder


def get_app_list(self, request):
    custom_order = [
        'New Orders',
        'Ready To Start Orders',
        'Being Delivered Orders',
        'Delivered Orders',
        'Not Pick Up Phone Orders',
        'Canceled Orders',
        'Archived Orders'

    ]
    app_dict = self._build_app_dict(request)
    app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())
    for app in app_list:
        if app['app_label'] == 'orders':
            app['models'].sort(key=lambda x: custom_order.index(x['name']))
    return app_list


admin.AdminSite.get_app_list = get_app_list


@admin.register(NewOrder)
class NewOrderModelAdmin(ModelAdmin):
    pass


@admin.register(ReadyToStartOrder)
class ReadyToStartOrderModelAdmin(ModelAdmin):
    pass


@admin.register(BeingDeliveredOrder)
class BeingDeliveredOrderModelAdmin(ModelAdmin):
    pass


@admin.register(NotPickUpPhoneOrder)
class NotPickUpPhoneOrderModelAdmin(ModelAdmin):
    pass


@admin.register(CanceledOrder)
class CancedOrderModelAdmin(ModelAdmin):
    pass


@admin.register(ArchivedOrder)
class ArchivedOrderModelAdmin(ModelAdmin):
    pass
