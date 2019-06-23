from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse


def home(request):
    return render(request, 'home')


def signup(request):
    if request.method == 'POST':
        user = User.objects.create_user(request.POST['firstname'], password=request.POST['phonenumber'])
        auth.login(request,user)
    return render(request, 'account/signup.html')


def login(request):
    if request.method == "POST":
        user = auth.authenticate(username = request.POST['username'] , passsword = request.POST['password'])
        if user is not None:
            auth.login(request , user)
            return redirect('account/signup.html')
        else:
            return render(request , 'account/login.html' , {'error' : 'Username or password is incorrect'})
    else:
        return render(request, 'account/login.html')
