from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime
from Home.models import Register
from django.contrib.messages import constants as messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


# Create your views here.
def home(request):
     return render(request, 'home.html')
def aboutus(request):
    return render(request, 'aboutus.html')
    # return HttpResponse("Ths is About page")

def gallery(request):
     return render(request, 'gallery.html')
def chatbox(request):
     return render(request, 'chatbox.html')

def events(request):
     return render(request, 'events.html')
def feedback(request):
     return render(request, 'feedback.html')

def profile(request):
     return render(request, 'profile.html')

def register(request):
     if request.method == "POST":
          firstname =  request.POST.get('firstname')
          lastname =   request.POST.get('lastname')
          phoneno =   request.POST.get('phoneno')
          email =   request.POST.get('email')
          password =   request.POST.get('password')
          usertype =   request.POST.get('usertype')
          address =   request.POST.get('address')
          address2 =   request.POST.get('address2')
          city =   request.POST.get('city')
          state =   request.POST.get('state')
          zip =   request.POST.get('zip')
          college =   request.POST.get('college')
          department =   request.POST.get('department')
          yop =   request.POST.get('yop')
          register = Register(firstname=firstname, lastname=lastname, phoneno=phoneno, email=email, password=password, usertype=usertype, address=address,address2=address2, city=city, state=state, zip=zip, college=college, department =department, yop=yop)
          register.save()
          # messages.success(request, 'Data Saved Scucessfully')
     
     return render(request, 'register.html')

def loginuser(request):
     # if request.method == "POST":
     #      # check if user has entered correct credentials
          username = request.POST.get('username')
          password = request.POST.get('password')
          print(username,password)
          user = authenticate(username = username, password= password)
          if user is not None:
               login(request, user)
               return render(request, 'home.html')
    # A backend authenticated the credentials
             
          else:
               return render(request, 'login.html')
    # No backend authenticated the credentials

     

def logoutuser(request):
     logout(request)
     return redirect("/selectusertype")

def selectusertype(request):
     return render(request, 'selectusertype.html')

   