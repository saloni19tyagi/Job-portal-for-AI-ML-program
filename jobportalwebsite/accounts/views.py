from django.shortcuts import render ,redirect
from .forms import UserRegisterForm
from django.http import HttpResponseRedirect , HttpResponse
from django.contrib import messages
from .models import Register

def register(request) :
	if request.method == "POST" :
		form = UserRegisterForm(request.POST)
		if form.is_valid() :
			form.save()
			name = form.cleaned_data.get('name')
			# email = form.cleaned_data.get('email')
			messages.success(request, f'Account created for {name}!')
			
			return redirect('register')
	else :
		form = UserRegisterForm()
	return render(request,'accounts/register.html' ,{'form' : form})


def login(request) :
	if request.method == "POST" :
		user_email = request.POST.get('email')
		user_password = request.POST.get('password')
		user1 = Register.objects.filter(email = user_email , password = user_password , is_valid = True , is_active = False)
		print(user1)
		if user1.exists() :
			user1.is_active = True
			# user1.save()
			request.session['email'] = user_email
			# request.session['password'] = user_password
			return render(request,'accounts/register.html')
		else :
			messages.error(request , f'Invalid Email or password!')
			return redirect('login')
	
	return render(request,'accounts/login.html')

def logout(request) :
	request.session['email'] = None
	# request.session['password'] = None
	return HttpResponse("<strong>You are logged out.</strong>")
