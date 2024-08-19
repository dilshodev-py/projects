from django.db.models import Manager
from apps.models import Order


class CustomOrderManager(Manager):
    def __init__(self, status_filter):
        super().__init__()
        self._set_creation_counter()
        self.model = None
        self.name = None
        self._db = None
        self._hints = {}
        self.status_filter = status_filter

    def get_queryset(self):
        return super().get_queryset().filter(status=self.status_filter)


class NewOrder(Order):
    objects = CustomOrderManager(status_filter=Order.Status.NEW)

    class Meta:
        proxy = True
        verbose_name = 'New Order'
        verbose_name_plural = 'New Orders'


class ReadyToStartOrder(Order):
    objects = CustomOrderManager(status_filter=Order.Status.READY_TO_START)

    class Meta:
        proxy = True
        verbose_name = 'Ready To Start Order'
        verbose_name_plural = 'Ready To Start Orders'


class BeingDeliveredOrder(Order):
    objects = CustomOrderManager(status_filter=Order.Status.BEING_DELIVERED)

    class Meta:
        proxy = True
        verbose_name = 'Being Delivered Order'
        verbose_name_plural = 'Being Delivered Orders'


class DeliveredOrder(Order):
    objects = CustomOrderManager(status_filter=Order.Status.DELIVERED)

    class Meta:
        proxy = True
        verbose_name = 'Delivered Order'
        verbose_name_plural = 'Delivered Orders'

class NotPickUpPhoneOrder(Order):
    objects = CustomOrderManager(status_filter=Order.Status.NOT_PICK_UP_PHONE)

    class Meta:
        proxy = True
        verbose_name = 'Not Pick Up Phone Order'
        verbose_name_plural = 'Not Pick Up Phone Orders'


class CanceledOrder(Order):
    objects = CustomOrderManager(status_filter=Order.Status.CANCELED)

    class Meta:
        proxy = True
        verbose_name = 'Canceled Order'
        verbose_name_plural = 'Canceled Orders'

class ArchivedOrder(Order):
    objects = CustomOrderManager(status_filter=Order.Status.ARCHIVED)

    class Meta:
        proxy = True
        verbose_name = 'Archived Order'
        verbose_name_plural = 'Archived Orders'
