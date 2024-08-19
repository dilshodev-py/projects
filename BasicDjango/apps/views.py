from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse

from apps.models import Product, Staff, Speaker, Region, District


# def nums_view(request):
#     result = ""
#     for i in range(1, 11):
#         result += f"{i}\n"
#     return HttpResponse(result)
#
#
# def order_list_view(request):
#     return TemplateResponse(request, 'apps/order_list.html')
#
#
# def advisors_list_view(request):
#     return TemplateResponse(request, 'apps/advisors_list.html')

def product_list_view(request):
    context = {
        "products": Product.objects.all()
    }
    return TemplateResponse(request, 'apps/product-list.html', context=context)


def order_list_view(request):
    context = {
        "products": Product.objects.all()
    }
    return TemplateResponse(request, 'apps/order-list.html', context=context)


def team_list_view(request):
    context = {
        "staffs": Staff.objects.all()
    }
    return TemplateResponse(request, 'apps/team-list.html', context=context)


def event_list_view(request):
    context = {
        "speakers": Speaker.objects.all()
    }
    return TemplateResponse(request, 'apps/event-list.html', context=context)


def icon_list_view(request):
    return TemplateResponse(request, 'apps/icons-list.html')


def region_list_view(request):
    context = {
        "regions": Region.objects.all()
    }
    return TemplateResponse(request, 'apps/region-list.html', context=context)


def district_list_view(request , pk : int):
    context = {
        "districts": District.objects.filter(region_id=pk)
    }
    return TemplateResponse(request, 'apps/district-list.html', context=context)
