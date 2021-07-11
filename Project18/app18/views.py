from django.shortcuts import render
from app18.forms import EmployeeRegistrationForm

# Create your views here.
def showIndex(request):
    return render(request,"index.html")


def addEmployee(request):
    emp = EmployeeRegistrationForm()
    return render(request,"addemployee.html",{"form":emp})


def saveemployee(request):
    id = request.POST.get("idno")
    na = request.POST.get("name")
    sal = request.POST.get("salary")
    des = request.POST.get("designation")

    print(id,na,sal,des,sep="\n")

    return None