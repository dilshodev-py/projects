from django.urls import path

from apps.views import product_list_view, order_list_view, team_list_view, event_list_view, icon_list_view, \
    region_list_view, district_list_view

# from apps.views import nums_view, order_list_view, advisors_list_view

urlpatterns = [
    # path("nums" , nums_view),
    # path("orders" , order_list_view),
    # path("advisors" , advisors_list_view),
    path('product-list' , product_list_view),
    path('order-list' , order_list_view),
    path('team-list' , team_list_view),
    path('event-list' , event_list_view),
    path('icon-list' , icon_list_view),
    path('regions-list' , region_list_view , name = "regions"),
    path('district-list/<int:pk>' , district_list_view , name = 'd'),
]