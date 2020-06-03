import datetime
import json

from django.http import HttpResponse
from django.shortcuts import render
from APIS import get_temperature_observatory as get_temp
from django.views.decorators.csrf import csrf_exempt
from applications.models import Temperature
from my_webpage import settings
import os



