from django.urls import path
from common import views

urlpatterns = [
    path("",views.showIndex,name = 'common_page'),
    path("student/",views.showStudent,name = 'student'),
    path("faculty/",views.showFaculty,name = 'faculty'),
    path("admin/",views.showAdmin,name = 'admin'),
]