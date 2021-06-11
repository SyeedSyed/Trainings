from django.shortcuts import render
from django.http import HttpResponse

def showIndex(request):
    if request.method=='POST':
        uname = request.POST.get('t1')
        pwd = request.POST.get('t2')

        if(uname=='Ravi') and (pwd=='12345'):
            return render(request,'index.html',{"status":"valid"})
        else:
            return render(request, 'index.html', {"status": "invalid"})

    if request.method=='GET':
        return render(request,'index.html')


