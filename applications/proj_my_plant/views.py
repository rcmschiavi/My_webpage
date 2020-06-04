from django.shortcuts import render

from . import get_format_data as get_data


def application_page(request):
    data = get_data.get_data_models()
    print(data)
    context = {
        'listData': data[0],
        'execution_time': data[1]
    }
    return render(request, 'my_plant.html', context)