from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse


def signup(request):
    if request.method == 'POST':
        user = User.objects.create_user(request.POST['firstname'], password=request.POST['phonenumber'])
        auth.login(request,user)
    return render(request, 'account/signup.html')

