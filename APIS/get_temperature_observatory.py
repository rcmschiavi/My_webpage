import requests
import json
import os

def get_json():
    API_ID = os.getenv('API_ID_OBSERVATORY')
    full_json = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Cacoal&appid='+API_ID)
    full_json = json.loads(full_json.text)
    return full_json['main']['temp'], full_json['dt']