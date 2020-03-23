from django import forms
from .models import *

class Projectform(forms.Form):
	MY_CHOICES = ()
	x=SIG.objects.all()
	for i in x:
		MY_CHOICES += ((i.pk, str(i.name)),)
	SIG=forms.ChoiceField(choices=MY_CHOICES)
	Name=forms.CharField(max_length=100)
	Description=forms.CharField(max_length=500)	
	Report_link=forms.CharField(max_length=250,required=False)
	Poster_link=forms.CharField(max_length=250,required=False)

class PasswordForm(forms.Form):
    key = forms.CharField(max_length=100)


class EventsForm(forms.Form):
	MY_CHOICES = ()
	x=(SIG.objects.all())
	for i in x:
		MY_CHOICES+=((i.pk, str(i.name)),)
	SIG=forms.ChoiceField(choices=MY_CHOICES)
	Name=forms.CharField(max_length=100)
	Description=forms.CharField(max_length=500)
