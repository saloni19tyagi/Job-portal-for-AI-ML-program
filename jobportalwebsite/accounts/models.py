from django.db import models
from django.db.models import IntegerField

class Register(models.Model) :
	first_name = models.CharField(max_length = 50, default = "")
	last_name = models.CharField(max_length = 50, default = "")
	email = models.EmailField(max_length = 50)
	mobile_number = models.IntegerField(default = "")
	city = models.CharField(max_length = 50 , default = "")
	tenth_marks = models.CharField(max_length = 50,default ="")
	twelfth_marks = models.CharField(max_length = 50,default = "")
	grad_year = models.IntegerField(default="")

	# resume = models.FileField(default = "")
