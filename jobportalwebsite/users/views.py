from django.shortcuts import render ,redirect
from django.contrib import messages
from .form import UserRegisterForm
from django.contrib.auth.decorators import login_required

from jobopening.models import JobOpening


def register(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid() :
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! You are now able to login')
			return redirect('login')
	else :
		form = UserRegisterForm
	return render(request,'users/register.html' ,{'form' : form})


@login_required
def profile(request):
	return render(request, 'users/profile.html')


def home(request):
	if request.method == "GET":
		k=JobOpening.objects.filter(isActive=1)
		return render(request,"users/home.html",{'values': k})