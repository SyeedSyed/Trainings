import urllib
import io
import matplotlib.pyplot as plt
from django.db.models import Q
from django.shortcuts import render
from student.models import RegistrationModel
from django.shortcuts import redirect
from common.utils import utils as ut
from django.contrib import messages
import pandas as pd
import numpy as np
import seaborn as sns
import base64
# from base64 import b64encode
import matplotlib
matplotlib.use('Agg')


def showIndex(request):
    return render(request, 'common/index.html')


def showStudent(request):
    return render(request, 'common/student.html')


def showRegistration(request):
    if request.method == "POST":
        name = request.POST.get('student_name')
        email = request.POST.get('student_email')
        contact = request.POST.get('student_contact')
        password = request.POST.get('student_password')

        record = RegistrationModel.objects.filter(
            Q(std_contact=contact) | Q(std_email=email))
        if record:
            return render(request, 'common/student.html', {"data": [name, email, contact, "Already Registered"]})
        else:
            otp = ut.getOTP()
            message = "Hi " + name + " Request has been initiated for email : " + \
                email + ". Use below OTP to verify request. OTP Generated is : " + \
                str(otp)

            if(ut.sendSMS(message, str(contact))):
                RegistrationModel(std_name=name,
                                  std_email=email,
                                  std_contact=contact,
                                  std_password=password,
                                  std_otp=otp).save()
                messages.success(request, str(contact))
                return redirect('student_otp')
            else:
                return render(request, 'common/student.html', {"data": [name, email, contact, "OTP Send Failed"]})
    else:
        showStudent(request)


def openStudentOtp(request):
    return render(request, 'common/otp.html')


def showFaculty(request):
    return render(request, 'common/faculty.html')


def showAdmin(request):
    return render(request, 'common/ocr_admin.html')


def validateOTP(request):
    if request.method == 'POST':
        contact = request.POST.get("contact")
        student_otp = request.POST.get("student_otp")
        try:
            result = RegistrationModel.objects.get(
                std_contact=contact, std_otp=student_otp)
            result.std_otp_sts = 'Active'
            result.save()
            return render(request, 'common/student.html', {"success": "Registration Successful"})
        except RegistrationModel.DoesNotExist:
            messages.success(request, contact)
            return redirect('student_otp')

    return render(request, 'common/otp.html')


def openRunChart(request):
    x = ['Jan', 'Feb', 'Mar']
    y = [1000, 1200, 900]

    plt.bar(x, y,
            width=0.8, color=['red', 'yellow', 'green'])

    plt.xlabel('x - axis')

    plt.ylabel('y - axis')

    plt.title('My bar chart!')

    plt.style.use('fivethirtyeight')

    fig = plt.gcf()
    # plt.close()

    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())

    uri = urllib.parse.quote(string)

    # context={'imgdata':uri}

    return render(request, 'common/chartDemo.html', {'graph': uri})


# def openRunChart(request):
#     x = ['Jan', 'Feb', 'Mar']
#     y = [1000, 1200, 900]

#     plt.bar(x, y,
#             width=0.8, color=['red', 'yellow', 'green'])

#     plt.xlabel('x - axis')

#     plt.ylabel('y - axis')

#     plt.title('My bar chart!')

#     plt.style.use('fivethirtyeight')

#     fig = plt.gcf()
#     plt.close()

#     buf = io.BytesIO()
#     fig.savefig(buf, format='png')
#     buf.seek(0)
#     string = base64.b64encode(buf.read())

#     uri = urllib.parse.quote(string)

#     # context={'imgdata':uri}

#     return render(request, 'common/chartDemo.html', {'graph': uri})
