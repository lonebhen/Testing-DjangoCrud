from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField()
    price = models.IntegerField()