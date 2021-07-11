from django.urls import path
from common import views

urlpatterns = [

    path('', views.showIndex, name='common_page'),
    path('common_student/', views.showStudent, name='student'),
    path('common_faculty/', views.showFaculty, name='faculty'),
    path('common_ocr_admin/', views.showAdmin, name='ocr_admin'),
    path('student_registration/', views.showRegistration,
         name='student_registration'),

    path('student_otp/', views.openStudentOtp, name='student_otp'),
    path('validate_otp/', views.validateOTP, name='validate_otp'),
    path('runchart/', views.openRunChart, name='runchart'),



]
