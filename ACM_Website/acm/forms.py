from django import forms
from .models import *

class Projectform(forms.Form):
	MY_CHOICES = ()
	x=len(SIG.objects.all())
	for i in range(x):
		MY_CHOICES += ((i+1, str(SIG.objects.get(pk=i+1).name)),)
	SIG=forms.ChoiceField(choices=MY_CHOICES)
	Name=forms.CharField(max_length=100)
	Description=forms.CharField(max_length=500)	
	Report_link=forms.CharField(max_length=250)
	Poster_link=forms.CharField(max_length=250)

class PasswordForm(forms.Form):
    key = forms.CharField(max_length=100)


class EventsForm(forms.Form):
	MY_CHOICES = ()
	x=len(SIG.objects.all())
	for i in range(x):
		MY_CHOICES+=((i+1, str(SIG.objects.get(pk=i+1).name)),)
	SIG=forms.ChoiceField(choices=MY_CHOICES)
	Name=forms.CharField(max_length=100)
	Description=forms.CharField(max_length=500)
