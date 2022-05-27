from django.db import models


# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=50)


class Goods(models.Model):
    goods_name = models.CharField(max_length=200)
    income_date = models.DateField()
    price = models.FloatField(default=0)
    measure_type = models.CharField(max_length=20)
    producer_name = models.CharField(max_length=200)
    category = models.ManyToManyField(Category)
