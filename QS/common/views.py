from django.shortcuts import render

def showMain(request):
    return render(request,'common/main.html')

def showMemberLogin(request):
    return render(request, 'common/memberlogin.html')


# def showMemberRegistration(request):
#     return render(request,'common/memberregistration.html')