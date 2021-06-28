from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=30, null=False)
    contact = models.IntegerField(unique=True, max_length=10, null=False) #Length not mandatory for integer.
    location = models.CharField(max_length=30, null=False)
    email = models.CharField(unique=True,max_length=30, null=False)
    password = models.CharField(max_length=30, null=False)




