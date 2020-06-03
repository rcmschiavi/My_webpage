import json
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from applications.models import My_plant_data

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
        if post_hash == settings.SENSOR_HASH_POSTING:
            temp = data['temperatura']
            humidity = data['umidade']
            moisture = data['umidade_solo']
            data_db = My_plant_data(TEMPERATURE=temp, HUMIDITY=humidity, MOISTURE=moisture)
            data_db.save()
            print("A temperatura é: {0}C, a umidade é: {1} e a umidade do solo eh: {2}".format(temp,humidity,moisture))

            return HttpResponse(200)
        else:
            return HttpResponse("You haven't provide the right HASH.")