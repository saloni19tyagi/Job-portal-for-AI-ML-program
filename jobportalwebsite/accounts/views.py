from django.shortcuts import render ,redirect
from .forms import UserRegisterForm , CompanyRegisterForm
from django.http import HttpResponseRedirect , HttpResponse
from django.contrib import messages
from .models import Register , Company

def dashboard(request) :
	# return HttpResponse("gdcyd")
	
	return render(request ,'accounts/dashboard.html')
	# return render(request,'accounts/register.html')


def company(request) :
	if request.method == "POST" :
		form = CompanyRegisterForm(request.POST)
		if form.is_valid() :
			form.save()
			name = form.cleaned_data.get('name')
			messages.success(request, f'Account created for Company {name}!')
			return redirect('jobopening')
	else :
		form = CompanyRegisterForm()
	return render(request,'accounts/company.html',{'form' : form})


def register(request) :
	if request.method == "POST" :
		form = UserRegisterForm(request.POST)
		if form.is_valid() :
			form.save()
			name = form.cleaned_data.get('name')
			# email = form.cleaned_data.get('email')
			messages.success(request, f'Account created for {name}!')
			
			return redirect('home')
	else :
		form = UserRegisterForm()
	return render(request,'accounts/register.html' ,{'form' : form})


def login(request) :
	if request.method == "POST" :
		if 'choice1' in request.POST :
			company_email = request.POST.get('email')
			company_password = request.POST.get('password')
			company1 = Company.objects.filter(email = company_email , password= company_password , is_valid = True)
			if company1.exists() :
				print(company)
				request.session['email'] = company_email
				return redirect('jobopening')
				# return render(request , 'opening/jobopening.html')
			else :
				messages.error(request , f'Invalid Email or password!')
				return render(request ,'accounts/login.html')

		if 'choice2' in request.POST :
			user_email = request.POST.get('email')
			user_password = request.POST.get('password')

			user1 = Register.objects.filter(email = user_email , password= user_password , is_valid = True ,is_active = False)
			if user1.exists() :
				user1.is_active = True
				request.session['email'] = user_email
				return redirect('home')
				# return render(request,'opening/home.html')
			else :
				messages.error(request , f'Invalid Email or password!')
				return render(request ,'accounts/login.html')

	return render(request,'accounts/login.html')

def logout(request) :
	request.session['email'] = None
	print(logout)
	# request.session['password'] = None
	return render(request ,'accounts/logout.html')
