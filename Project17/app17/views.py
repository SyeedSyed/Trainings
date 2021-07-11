from django.shortcuts import render, redirect
from app17.models import StudentDetailsModel

# Create your views here.


def showIndex(request):
    return render(request, "index.html",)


def saveStudent(request):
    if request.method == "POST":
        name = request.POST.get("name")
        cno = request.POST.get("contact")
        photo = request.FILES['photo']
        dob = request.POST.get('DOB')
        email = request.POST.get("email")
        password = request.POST.get("password")

        StudentDetailsModel(name=name, contact=cno, photo=photo,
                            dob=dob, email=email, password=password).save()

        return redirect('main')


def showAdmin(request):
    return render(request, "admin.html", {"students_info": StudentDetailsModel.objects.all()})


def delStudent(request, student_number):
    student_data = StudentDetailsModel.objects.get(number=student_number)
    if request.method == "POST":
        student_data.delete()
        return render(request, "admin.html", {"students_info": StudentDetailsModel.objects.all()})
    else:
        return render(request, "delete_student.html", {"student_info": student_data})


def updStudent(request, student_number):
    student_data = StudentDetailsModel.objects.get(number=student_number)
    if request.method == "POST":
        cno = request.POST.get("student_contact")
        email = request.POST.get("student_email")
        updflg = False
        print(student_data.contact)
        print(student_data)
        print(cno)
        if student_data.contact != cno:
            student_data.contact = cno
            global Y
            updflg = True

        if student_data.email != email:
            student_data.email = email
            global Y
            updflg = True

        if(updflg):
            student_data.save()

        return render(request, "admin.html", {"students_info": StudentDetailsModel.objects.all()})
    else:
        return render(request, "update_student.html", {"student_info": student_data})
