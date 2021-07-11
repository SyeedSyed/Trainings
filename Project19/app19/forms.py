
from django import forms
from app19.models import EmployeeRegistrationModel


class EmployeeRegistrationForm(forms.ModelForm):
    des = (
        ('Manager','Manager'),
        ('Developer','Developer'),
        ('Designer','Designer'),
    )
    salary = forms.FloatField(min_value=10000)
    designation = forms.ChoiceField(choices=des)

    class Meta:
        model = EmployeeRegistrationModel
        fields = "__all__"
        labels = {"dob":"Date of Birth"}