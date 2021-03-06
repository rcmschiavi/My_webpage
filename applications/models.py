from django.db import models



class Temperature(models.Model):
    TEMPERATURE = models.DecimalField(max_digits=5, decimal_places=2)
    REGISTERED_AT = models.DateTimeField(auto_now=True)
    TEMPERATURE_OBSERVATORY = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    TIME_OBSERVATORY = models.DateTimeField(auto_now=False, null=True)
    class Meta:
       managed = True
       db_table = 'TEMPERATURE'

    def __str__(self):
        return 'Time: ' + str(self.REGISTERED_AT)


class My_plant_data(models.Model):
    TEMPERATURE = models.DecimalField(max_digits=5, decimal_places=2)
    HUMIDITY = models.DecimalField(max_digits=5, decimal_places=2)
    MOISTURE = models.DecimalField(max_digits=5, decimal_places=2)
    REGISTERED_AT = models.DateTimeField(auto_now=True)
    class Meta:
       managed = True
       db_table = 'AGRICULTURE'

    def __str__(self):
        return 'Time: ' + str(self.REGISTERED_AT)