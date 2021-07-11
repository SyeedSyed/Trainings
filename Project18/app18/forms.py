
from django import forms

class EmployeeRegistrationForm(forms.Form):

    desg = (
        ('Manager','MANAGER'),
        ('Developer','DEVELOPER'),
        ('QA','QA')
    )

    idno = forms.IntegerField(label="EMPLOYEE Number")
    name = forms.CharField(label="Employee Name")
    salary = forms.FloatField(label="Employee Salary")

    designation1 = forms.ChoiceField(label="Employee Designation",choices=desg)

    designation2 = forms.ChoiceField(label="Employee Designation",choices=desg,widget=forms.RadioSelect)

    c = forms.CharField(label="C Language",widget=forms.CheckboxInput)
    python = forms.CharField(label="Python",widget=forms.CheckboxInput)
    java = forms.CharField(label="Java",widget=forms.CheckboxInput)

    photo = forms.ImageField(label="Employee Photo")


    dob = forms.DateField(label="Employee Data of Birth")
    email = forms.EmailField(label="Employee Email Id")
    password = forms.CharField(label="Employee Password",widget=forms.PasswordInput)


