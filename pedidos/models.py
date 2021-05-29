
from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.db.models.fields import AutoField


class Client(models.Model):
    ID = models.AutoField(primary_key=True)
    NAME = models.TextField()
    class Meta:
       managed = True

    def __str__(self):
        return self.NAME


class Product(models.Model):
    ID = models.AutoField(primary_key=True)
    NAME = models.TextField()
    SUGESTED_PRICE = models.DecimalField(max_digits=10, decimal_places=2)
    MULTIPLIER = models.PositiveIntegerField(default=1)
    class Meta:
       managed = True

    def __str__(self):
        return self.NAME


class Order(models.Model):
    ID = models.AutoField(primary_key=True)
    CLIENT = models.ForeignKey(Client, on_delete=models.CASCADE)
    PRODUCTS = models.ManyToManyField(Product, through="OrderDetails")
    class Meta:
       managed = True

    def __str__(self):
        return "Order ID: " + str(self.ID)


class OrderDetails(models.Model):
    PRODUCT = models.ForeignKey(Product, on_delete=models.CASCADE)
    ORDER = models.ForeignKey(Order, on_delete=models.CASCADE)
    QUANTITY = models.PositiveIntegerField()

    