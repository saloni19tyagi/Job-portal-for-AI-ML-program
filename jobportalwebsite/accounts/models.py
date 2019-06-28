from django.db import models
from django.db.models import IntegerField
from phonenumber_field.modelfields import PhoneNumberField

class Register(models.Model) :


	name = models.CharField(max_length = 50, default = "")
	email = models.EmailField(max_length = 50, primary_key = True)
	mobile_number = PhoneNumberField()
	city = models.CharField(max_length = 50 , default = "")
	tenth_marks = models.IntegerField(default ="")
	twelfth_marks = models.IntegerField(default = "")
	course = models.CharField(max_length = 50,default = "")
	college_name = models.CharField(max_length = 100,default = "")
	stream = models.CharField(max_length = 50,default = "")
	graduation_year = models.IntegerField(default = "")
	is_valid = models.BooleanField(default = False)
	is_active = models.BooleanField(default = False)
	password = models.CharField(default = "" ,max_length = 50)

	def __str__(self):
		return self.name

class Login(models.Model):

	id = models.AutoField(primary_key=True)

class Company(models.Model) :
	name = models.CharField(max_length = 50, default = "")
	email = models.EmailField(max_length = 50,primary_key=True)
	mobile_number = PhoneNumberField(default="")
	details = models.TextField()
	is_valid = models.BooleanField(default = False)
	password = models.CharField(default = "" ,max_length = 50)
	
