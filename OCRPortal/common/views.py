from django.shortcuts import render
from student.models import RegistrationModel
from django.shortcuts import redirect
from common.utils import utils as ut

def showIndex(request):
    return render(request,'common/index.html')

def showStudent(request):
    return render(request,'common/student.html')

def showRegistration(request):
    if request.method=="POST":
        name = request.POST.get('student_name')
        email = request.POST.get('student_email')
        contact = request.POST.get('student_contact')
        password = request.POST.get('student_password')

        otp = ut.getOTP()

        message = "Hi " + name + " Request to debit Rs50,000 from your account has been initiated for email : " + email + ". Use below OTP to verify request. OTP Generated is : " + str(otp)

        if(ut.sendSMS(message, str(contact))):
            RegistrationModel(std_name = name,
                          std_email=email,
                          std_contact=contact,
                          std_password=password,
                          std_otp=otp).save()
        else:
            return render(request,'common/student.html',{'message':"OTP Send Failed"})

        return redirect('student_otp')
    else:
        showStudent(request)

def openStudentOtp(request):
    return render(request,'common/otp.html')

def showFaculty(request):
    return render(request,'common/faculty.html')

def showAdmin(request):
    return render(request,'common/ocr_admin.html')
