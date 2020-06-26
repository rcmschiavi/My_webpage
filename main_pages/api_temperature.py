"""

My ESP8266 is old and had some kind of issue with its UART IC, so I could not update firmware with the new url for
the temperature request. It takes a month to the brazilian governmental delivery sh*t company to deliver one for me,
so I solved with what we call here as a "gambiarra", which means a non-conventional technical solution.

"""

import datetime
import json
import pytz
from django.http import HttpResponse, JsonResponse
from APIS import get_temperature_observatory as get_temp
from django.views.decorators.csrf import csrf_exempt
from applications.models import Temperature
import os


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
            response = 200
            try:
                temp_observatory, time_observatory = get_temp.get_json()
                temp_observatory = temp_observatory - 273.15
                time_observatory_dt = datetime.datetime.fromtimestamp(time_observatory)
                data_db = Temperature(TEMPERATURE=temp, TEMPERATURE_OBSERVATORY=temp_observatory,
                                      TIME_OBSERVATORY=time_observatory_dt)
            except:
                data_db = Temperature(TEMPERATURE=temp)
                response = "There was an error at the observatory request, but the sensor data was stored."
            data_db.save()

            return HttpResponse(response)
        else:
            return HttpResponse("You haven't provide the right HASH.")



def update_temperature(request):
    tz = pytz.timezone('America/Porto_Velho')
    query = Temperature.objects.order_by('-REGISTERED_AT').first()
    context = {
        "My_data":{'temp': query.TEMPERATURE,
                   'time': query.REGISTERED_AT.astimezone(tz).__format__('%c')
                   },
        "Observatory_data":{'temp': query.TEMPERATURE_OBSERVATORY,
                            'time': query.TIME_OBSERVATORY.astimezone(tz).__format__('%c')
                            }
    }
    return JsonResponse(context)