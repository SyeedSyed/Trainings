from django.db import models

class EmployeeRegistrationModel(models.Model):
    number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=False)
    contact = models.IntegerField(unique=True)
    salary = models.FloatField(null=False)
    designation = models.CharField(max_length=100,null=False)
    dob = models.DateField(null=False)
    email = models.EmailField(max_length=100,null=False,default="")