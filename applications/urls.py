"""my_webpage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views# Create your views here.
def index(request):
    return render(request, 'index.html')

    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from .proj_temperature_chart import api as temp_api
from .proj_my_plant import api as plant_api

urlpatterns = [
    url('API/temperature_data', temp_api.post_temperature, name='post_temp'),
    url('API/my_plant_data', plant_api.post_my_plant_data, name='post_agriculture_data'),
]
