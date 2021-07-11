from django.shortcuts import render
from app19.forms import EmployeeRegistrationForm
from app19.models import EmployeeRegistrationModel

def showIndex(request):
    return render(request,"index.html")


def add_employee(request):
    emp = EmployeeRegistrationForm(request.POST)
    if request.method == "POST":
        # n = request.POST.get("name")
        # c = request.POST.get("contact")
        # s = request.POST.get("salary")
        # d = request.POST.get("designation")
        # dob = request.POST.get("dob")
        # e = request.POST.get("email")
        #
        # EmployeeRegistrationModel(name=n,contact=c,salary=s,designation=d,dob=dob,email=e).save()
        emp.save()
        return render(request, "add_employee.html", {"form": emp})
    else:
        return render(request,"add_employee.html",{"form":emp})