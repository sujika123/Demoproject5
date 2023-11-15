from django.urls import path

from demoapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('loginview',views.loginview,name='loginview'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('userhome',views.userhome,name='userhome'),
    path('profileview',views.profileview,name='profileview'),
    path('profileupdate/<int:id>/',views.profileupdate,name='profileupdate'),
    path('addeventuser',views.addeventuser,name='addeventuser'),
    path('viewevent',views.viewevent,name='viewevent'),
    path('eventdelete/<int:id>/',views.eventdelete,name='eventdelete'),
    path('eventupdate/<int:id>/',views.eventupdate,name='eventupdate'),
    path('userview',views.userview,name='userview'),
]