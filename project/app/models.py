from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=360)
    like = models.IntegerField(default=0)
    comment = models.CharField(max_length=1000)
    photo = models.ImageField(default='/static/shop/default/test.jpg')
    price = models.IntegerField(default=-0)
