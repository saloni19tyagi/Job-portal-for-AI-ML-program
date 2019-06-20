from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse

# Create your views here.
def signup(request):
    if request.method =='POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['firstname']
            number = form.cleaned_data['phonenumber']
            p = Person(firstname=firstname, phone_number=number, lastname=lastname)
            p.save()
        # if request.POST['password1'] == request.POST['password2']:
        #         try:
        #             user = User.objects.get(username=request.POST['username'])
        #             return render(request, 'account/signup.html', {'error':'Username has already been taken'})
        #         except User.DoesNotExist:
        #             user = User.objects.all(id=request.POST['phonenumber'])
        #             auth.login(request,user)
        #             return redirect('home')
        else:
            return render(request, 'account/signup.html', {'error':'Passwords must match'})
    else:
        return render(request, 'account/signup.html')

