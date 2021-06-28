from django.db import models

class RegistrationModel(models.Model):
    std_name = models.CharField(max_length=50,null=False)
    std_contact = models.IntegerField(unique=True,null=False)
    std_email = models.CharField(max_length=50,unique=True,null=False)
    std_password = models.CharField(max_length=20,null=False)
    std_otp = models.IntegerField(null=False,default=000000)
    std_otp_sts=models.CharField(max_length=10,default='Pending',null=False)
    std_reg_date = models.DateTimeField(auto_now_add=True)

