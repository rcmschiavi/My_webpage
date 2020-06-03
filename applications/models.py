from django.db import models

# Create your models here.

class Temperature(models.Model):
    TEMPERATURE = models.DecimalField(max_digits=5, decimal_places=2)
    REGISTERED_AT = models.DateTimeField(auto_now=True)
    TEMPERATURE_OBSERVATORY = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    TIME_OBSERVATORY = models.DateTimeField(auto_now=False, null=True)
    class Meta:
       managed = True
       db_table = 'TEMPERATURE'


class Agriculture_data(models.Model):
    TEMPERATURE = models.DecimalField(max_digits=5, decimal_places=2)
    HUMIDITY = models.DecimalField(max_digits=5, decimal_places=2)
    MOISTURE = models.DecimalField(max_digits=5, decimal_places=2)
    REGISTERED_AT = models.DateTimeField(auto_now=True)
    class Meta:
       managed = True
       db_table = 'AGRICULTURE'