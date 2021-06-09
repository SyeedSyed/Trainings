from django.shortcuts import render
from django.http import HttpResponse

def showIndex(request):
    return render(request, 'index.html')

def registerUser(request):
    userid = request.POST.get("x1")
    password = request.POST.get("x2")

    ulist = {"Syeed":"12345","Naveen":"12345","Alex":"54321"}

    if ulist[userid] == password:
        data = {"user":userid}
        return render(request,"welcome.html",data)
    else:
        return render(request,"error.html")

