from django.shortcuts import render
from django.http import HttpResponse
from inherapp.models import Registration

def showIndex(request):
    return render(request,'main.html')

def showRegister(request):
    if request.method=="POST":
        n = request.POST.get("name")
        c = request.POST.get("contact")
        l = request.POST.get("location")
        e = request.POST.get("email")
        p = request.POST.get("password")

        Registration(name=n,contact=c,location=l,email=e,password=p).save()

        return render(request,'register.html',{'message':'Registration is Successful'})
    else:
        return render(request,'register.html')

def showLogin(request):
    if request.method == "POST":
        e = request.POST.get("email")
        p = request.POST.get("password")

        try:
            logrec = Registration.objects.get(email=e,password=p)
            return render(request, 'welcome.html')
        except Registration.DoesNotExist:
            return render(request, 'login.html',{'err_msg':"Invalid Login"})

    else:
        return render(request, 'login.html')

def showUserHome(request):
    return render(request,'userHome.html')

def showManager(request):
    return render(request,'manager.html')

def showEmployee(request):
    return render(request,'employee.html')

def showSignout(request):
    return render(request,'login.html',{'so_msg':"Signed out successfully"})


