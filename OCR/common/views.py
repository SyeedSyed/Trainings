from django.shortcuts import render

def showIndex(request):
    return render(request,'common/index.html')

def showStudent(request):
    if(request.method=="POST"):
        message = request.POST.get("name")
        return render(request,'common/student.html',{'message':message})
    else:
        return render(request,'common/student.html')

def showFaculty(request):
    if(request.method=="POST"):
        message = request.POST.get("name")
        return render(request,'common/faculty.html',{'message':message})
    else:
        return render(request,'common/faculty.html')

def showAdmin(request):
    if(request.method=="POST"):
        message = request.POST.get("name")
        return render(request,'common/admin.html',{'message':message})
    else:
        return render(request,'common/admin.html')

