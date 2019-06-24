from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm) :
	Email = forms.EmailField()
	Contact_Number = forms.CharField()
	Resume = forms.FileField()

	class meta :
		model = User
		fields = ['username' ,'Email', 'Contact Number' ,'Resume','password' ,'password1']