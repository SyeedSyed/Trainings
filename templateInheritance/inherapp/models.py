from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=30)
    contact = models.IntegerField(unique=True, max_length=10)
    location = models.CharField(max_length=30)
    email = models.CharField(unique=True,max_length=30)
    password = models.CharField(max_length=30)




