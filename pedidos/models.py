
from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.db.models.fields import AutoField


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    class Meta:
       managed = True
       db_table = 'client'
    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    sugested_price = models.DecimalField(max_digits=10, decimal_places=2)
    multiplier = models.PositiveIntegerField(default=1)
    class Meta:
       managed = True
       db_table = 'product'
    def __str__(self):
        return self.name


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through="OrderDetails")
    class Meta:
       managed = True
       db_table = 'order'
    def __str__(self):
        return "Order ID: " + str(self.ID)


class OrderDetails(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    class Meta:
       managed = True
       db_table = 'order_details'
    