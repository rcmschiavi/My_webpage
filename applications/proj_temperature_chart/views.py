# coding: utf-8
from django.shortcuts import render
from . import get_format_data as get_data

def application_page(request):
    list_data = get_data.get_temp_by_hour()
    context = {
        'listData': list_data
    }
    return render(request, 'temperature_chart.html', context)
