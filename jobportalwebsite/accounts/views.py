from django.shortcuts import render ,redirect
from .forms import UserRegisterForm
from django.contrib import messages

def register(request) :
	if request.method == "POST" :
		form = UserRegisterForm(request.POST)
		if form.is_valid() :
			form.save()
			# first_name = form.cleaned_data.get('first_name')
			# email = form.cleaned_data,get('email')
			messages.success(request, f'Account created!')
			return redirect('register')
	else :
		form = UserRegisterForm()
	return render(request,'accounts/register.html' ,{'form' : form})
