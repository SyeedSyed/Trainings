from django.shortcuts import render
from django.http import HttpResponse

def showIndex(request):
    data = {"name":"Syeed","Salary":100000}
    return render(request, 'index.html',data)

def registerUser(request):
    f_name = request.POST.get("x1")
    l_name = request.POST.get("x2")
    full_name = f_name + " " + l_name
    #greet = "Welcome "
    #resp = greet + full_name
    #return HttpResponse(resp)
    ###
    data = {"fullname":full_name}
    return render(request, 'welcome.html',data)
    ###

