from django.db import models
from django.contrib import admin


class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    type = models.CharField(max_length=25)
    def __str__(self):
        return f"{self.name}"  

class Cart(models.Model):
    amount = models.IntegerField()
    allprice = models.IntegerField()
    def __str__(self):
        return self.amount

