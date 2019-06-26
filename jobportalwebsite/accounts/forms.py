from django import forms
from .models import Register


class UserRegisterForm(forms.ModelForm) :
	class Meta :
		model = Register
		fields = ['first_name' , 'last_name', 'email' , 'mobile_number' ,'city' ,'tenth_marks' , 'twelfth_marks' ,'grad_year']
