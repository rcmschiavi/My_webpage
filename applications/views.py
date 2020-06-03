import datetime
import json

from django.http import HttpResponse
from django.shortcuts import render
from APIS import get_temperature_observatory as get_temp
from django.views.decorators.csrf import csrf_exempt
from applications.models import Temperature
from my_webpage import settings
import os

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def post_temperature(request):

    if request.method == "POST":
        data = json.loads(request.body)

        try:
            post_hash = data['HASH']
        except KeyError:
            return HttpResponse("The data is not complete.")
        except Exception as e:
            return HttpResponse("Some error occured during the post. Exception: " + str(e))

        # A HASH provided by the devices to avoid users to create posts
        if post_hash == os.getenv('SENSOR_HASH_POSTING'):
            temp = data['temperatura']
            try:
                temp_observatory, time_observatory = get_temp.get_json()
                temp_observatory = temp_observatory-273.15
                time_observatory_dt = datetime.datetime.fromtimestamp(time_observatory)
                data_db = Temperature(TEMPERATURE=temp, TEMPERATURE_OBSERVATORY=temp_observatory,
                                      TIME_OBSERVATORY=time_observatory_dt)
            except:
                data_db = Temperature(TEMPERATURE=temp)
            data_db.save()

            return HttpResponse(200)
        else:
            return HttpResponse("You haven't provide the right HASH.")
