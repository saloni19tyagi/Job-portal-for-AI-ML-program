from django import forms
from django.forms import ModelForm


class Person(forms.Form):
  firstname = forms.CharField(label='firstame', max_length=100)
  phonenumber = forms.CharField(label='phonenumber', max_length=12, min_length=10)
  lastname = forms.CharField(label='firstame', max_length=100)

