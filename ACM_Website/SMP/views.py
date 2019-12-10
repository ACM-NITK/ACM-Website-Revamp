from django.shortcuts import render
from .models import *
from acm.models import *
from django.http import HttpResponse

def home(request,sig_id):
 si=SIG.objects.filter(pk=sig_id)
 sig=si[0]
 sigo=SIG.objects.all()
 smps=SMP.objects.filter(sig_id=sig_id)
 contex={ 'sig':sig, 'sigo':sigo, 'smps':smps }
 return render(request,'spms.html',contex)
def des(request,sig_id,smp_id):
 smp=(SMP.objects.filter(pk=smp_id))[0]
 smp_des=SMP_des.objects.filter(smp_id=smp_id)
 contex={ 'smp':smp, 'smp_des':smp_des }
 return render(request,'smp_des.html',contex)

