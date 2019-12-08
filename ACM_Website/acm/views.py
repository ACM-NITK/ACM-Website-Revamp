from django.shortcuts import render
from .models import *
from django.http import HttpResponse

def home_page(request):
	return HttpResponse('home page')

def sig_page(request, sig_id):
  sig=SIG.objects.filter(pk=sig_id)
  sigo=SIG.objects.all()
  events=Events.objects.filter(sig_id=sig_id)
  projects=Projects.objects.filter(sig_id=sig_id)
  contex = { 'sig': sig,'events': events, 'projects': projects, 'sigo': sigo }
  return render(request,'yantras.html',contex)
  
