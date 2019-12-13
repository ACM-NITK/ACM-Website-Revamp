from django import forms
from .models import *

class Projectform(forms.Form):
	def __init__(self, *args, **kwargs):
		super(Projectform, self).__init__(*args, **kwargs)
		MY_CHOICES = ()
		x=len(SIG.objects.all())
		for i in range(x):
			MY_CHOICES += ((i+1, str(SIG.objects.get(pk=i+1).name)),)
		self.fields['SIG']=forms.ChoiceField(choices=MY_CHOICES)
		self.fields['Name']=forms.CharField(max_length=100)
		self.fields['Description']=forms.CharField(max_length=500)	
		self.fields['Report_link']=forms.CharField(max_length=250)
		self.fields['Poster_link']=forms.CharField(max_length=250)

class PasswordForm(forms.Form):
    key = forms.CharField(max_length=100)


class EventsForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super(EventsForm, self).__init__(*args, **kwargs)
		MY_CHOICES = ()
		x=len(SIG.objects.all())
		for i in range(x):
			MY_CHOICES+=((i+1, str(SIG.objects.get(pk=i+1).name)),)
		self.fields['SIG']=forms.ChoiceField(choices=MY_CHOICES)
		self.fields['Name']=forms.CharField(max_length=100)
		self.fields['Description']=forms.CharField(max_length=500)
