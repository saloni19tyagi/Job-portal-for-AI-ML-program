from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm) :
    first_name = forms.CharField()
    middle_name = forms.CharField()
    last_name = forms.CharField()
    date_of_birth = forms.DateField()
    email = forms.EmailField()
    experience = forms.CharField()
    password1 = None
    password2 = None
    Contact_Number = forms.CharField()
    Resume = forms.FileField()

    class meta :
    	model = User
    	fields = ['username' ,'email', 'Contact Number' ,'Resume']



