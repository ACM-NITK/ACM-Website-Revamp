from django.shortcuts import render
from .models import *
from django.http import HttpResponse

def home_page(request):
	return HttpResponse('home page')

def sig_page(request, sig_id):
  si=SIG.objects.filter(pk=sig_id)
  sig=si[0]
  sigo=SIG.objects.all()
  events=Events.objects.filter(sig_id=sig_id)
  projects=Projects.objects.filter(sig_id=sig_id)
  contex = { 'sig': sig,'events': events, 'projects': projects, 'sigo': sigo }
  return render(request,'acm/yantras.html',contex)
def contact_us(request):
  sigo=SIG.objects.all()
  contex = {'sigo': sigo}
  return render(request,'acm/contact_us.html',contex)
def esp(request):
 sigo=SIG.objects.all()
 contex = {'sigo': sigo}
 return render(request,'acm/esp.html',contex) 

  
  
