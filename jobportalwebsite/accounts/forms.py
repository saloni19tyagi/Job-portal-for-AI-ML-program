from django import forms
from .models import Register , Company



class UserRegisterForm(forms.ModelForm) :
	COURSE = [
	('btech','BTech'),
	('be','BE'),
	('bsc','BSC'),
	('others','Ohers')
	]
	course = forms.CharField(label = "Select Your Course", widget = forms.Select(choices=COURSE))
	# password = forms.CharField(widget=PasswordInput())
	class Meta :
		model = Register
		fields = ['name', 'email' , 'mobile_number' ,'city' ,'tenth_marks' , 'twelfth_marks'  , 'course','college_name' ,'stream','graduation_year']


class CompanyRegisterForm(forms.ModelForm) :
	class Meta :
		model = Company
		fields = ['name' ,'email','details','mobile_number']