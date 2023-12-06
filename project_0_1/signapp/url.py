from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.loginpage,name='loginpage'),
   path('logout/',views.logout_user,name='logoutpage'),
   path('signup/',views.signpage,name='signpage'),
   path('home/',views.home,name='home')
   
]
