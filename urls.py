
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from Home import views

admin.site.site_header = "Alumni Portal for Department"
admin.site.site_title = "Welcome To Admin Section"
admin.site.index_title = "Welcome Alumni Portal "

urlpatterns = [
    path("", views.loginuser, name='loginuser'),
    path("aboutus", views.aboutus, name='aboutus'),
    path("gallery", views.gallery, name='gallery') ,
    path("home", views.home, name='home'),
    path("chatbox", views.chatbox, name='chatbox'),
    path("events", views.events, name='events'),
    path("feedback", views.feedback, name='feedback'),
    path("profile", views.profile, name='profile'),
    path("login", views.loginuser, name='login'),
    path("register", views.register, name='register'),
    path("logoutuser", views.logoutuser, name='logoutuser'),
    path("selectusertype", views.selectusertype, name='selectusertype') 
]
