from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Q
from django.views.generic import ListView

from apps.models import Stream


class StatisticListView(LoginRequiredMixin, ListView):
    queryset = Stream.objects.all()
    template_name = 'apps/order/statistika.html'
    context_object_name = 'streams'
    def get_queryset(self):
        qs = super().get_queryset().filter(user=self.request.user).select_related('product').annotate(
            new_count=Count('orders', filter=Q(orders__status='new')),
            ready_to_start_count=Count('orders', filter=Q(orders__status='ready_to_start')),
            being_delivered_count=Count('orders', filter=Q(orders__status='being_delivered')),
            delivered_count=Count('orders', filter=Q(orders__status='delivered')),
            not_pick_up_phone_count=Count('orders', filter=Q(orders__status='not_pick_up_phone')),
            canceled_count=Count('orders', filter=Q(orders__status='canceled'))
        ).values('name', 'product__name', 'count', 'new_count', 'ready_to_start_count', 'being_delivered_count',
                      'delivered_count','not_pick_up_phone_count' , 'canceled_count' )
        return qs


