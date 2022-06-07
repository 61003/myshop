from django.db import models
from django.db.models import Manager
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)
    objects = Manager()
    on_site = CurrentSiteManager('site')

class Goods(models.Model):
    goods_name = models.CharField(max_length=200)
    income_date = models.DateField()
    price = models.FloatField(default=0)
    measure_type = models.CharField(max_length=20)
    producer_name = models.CharField(max_length=200)
    category = models.ManyToManyField(Category)
    site = models.ManyToManyField(Site)
    objects = Manager()
    on_site = CurrentSiteManager('site')
