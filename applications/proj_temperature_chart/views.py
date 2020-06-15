# coding: utf-8
from django.shortcuts import render
from . import get_format_data as get_data

def application_page(request):
    list_data, days = get_data.get_temp_by_hour()
    first_day = [days[0].day, days[0].month, days[0].year]
    last_day = [days[1].day, days[1].month, days[1].year]
    context = {
        'listData': list_data,
        'days_date_picker': [first_day, last_day]
    }
    return render(request, 'temperature_chart.html', context)
