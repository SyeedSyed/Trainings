
from django.urls import path
from common import views

urlpatterns = [

    path('',views.showMain,name = 'showmain'),
    path('memberlogin/',views.showMemberLogin,name = 'memberlogin'),

    # path('member_registration/',views.showMemberRegistration,name = 'member_registration'),

]
