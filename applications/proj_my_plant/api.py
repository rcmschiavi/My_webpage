import json

import pytz
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from applications.models import My_plant_data
import os


@csrf_exempt
def post_my_plant_data(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        try:
            post_hash = data['HASH']
        except KeyError:
            return HttpResponse("The data is not complete.")
        except Exception as e:
            return HttpResponse("Some error occured during the post. Exception: " + str(e))

        # A HASH provided by the devices to avoid users to create posts
        if post_hash == os.getenv('SENSOR_HASH_POSTING'):
            temp = data['temperatura']
            humidity = data['umidade']
            moisture = data['umidade_solo']
            data_db = My_plant_data(TEMPERATURE=temp, HUMIDITY=humidity, MOISTURE=moisture)
            data_db.save()
            return HttpResponse(200)
        else:
            return HttpResponse("You haven't provide the right HASH.")


def update_my_plant(request):
    tz = pytz.timezone('America/Porto_Velho')
    query = My_plant_data.objects.order_by('-REGISTERED_AT').first()
    context = {'temp': query.TEMPERATURE,
               'humidity': query.HUMIDITY,
               'moisture': query.MOISTURE,
               'time': query.REGISTERED_AT.astimezone(tz).__format__('%c')
               }
    return JsonResponse(context)
