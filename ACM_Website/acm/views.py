from django.shortcuts import render
from .models import *
from django.http import HttpResponse

def home_page(request):
	return HttpResponse('home page')

def sig_page(request, sig_name):
	return HttpResponse(sig_name)
