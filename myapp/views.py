from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST' :
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password']
        c_password= request.POST['c_password']

        if c_password == password:
            if User.objects.filter(email = email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('signup')
            elif User.objects.filter(username = username).exists():
                messages.info(request,'Username Already Exists') 
                return redirect('signup')
            else:
                user = User.objects.create_user(username = username, email = email, password = c_password)
                user.save();
                return redirect('login')
        else: 
            messages.info(request, 'Password is not the same')
            return redirect('signup')
    else:
        return render (request, 'signup.html' )
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
