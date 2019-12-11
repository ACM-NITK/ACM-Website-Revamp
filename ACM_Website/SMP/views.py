from django.shortcuts import render
from .models import *
from acm.models import *
from django.http import HttpResponse
import json
from .forms import *
from django.shortcuts import redirect
from django.contrib import messages

def home(request,sig_id):
 si=SIG.objects.filter(pk=sig_id)
 sig=si[0]
 sigo=SIG.objects.all()
 smps=SMP.objects.filter(sig_id=sig_id)
 with open('acm/static/acm/json/smp.json') as f:
        data2 = json.loads(f.read())
        data =''
        for i in range (5):
            if(int(data2[i]['id'])==sig_id):
                data=data2[i]
 contex={ 'sig':sig, 'sigo':sigo, 'smps':smps, 'data':data}
 return render(request,'spms.html',contex)
def des(request,sig_id,smp_id):
 smp=(SMP.objects.filter(pk=smp_id))[0]
 smp_des=SMP_des.objects.filter(smp_id=smp_id)
 contex={ 'smp':smp, 'smp_des':smp_des }
 return render(request,'smp_des.html',contex)


def new_smp(request):
    validated = 0
    if request.method == "POST":
        password_form = PasswordForm(request.POST)
        smp_form = SMPForm(request.POST)
        if smp_form.is_valid():
            print("hi")
            sig = smp_form.cleaned_data["SIG"]
            name = smp_form.cleaned_data["Name"]
            mentors = smp_form.cleaned_data["Mentors"]
            overview = smp_form.cleaned_data["Overview"]
            platform = smp_form.cleaned_data["Platform"]

            if sig:
                SMP_object = SMP.objects.create(
                    sig_id=SIG.objects.get(pk=sig), name=name, mentors=mentors, overview=overview, platform_of_tutoring=platform)

                SMP_object.save()

            for i in range(smp_form.cleaned_data["exercise_freq"]):
                des = smp_form.cleaned_data["Exercise_"+str(i+1)]
                if des:
                    SMP_des_object = SMP_des.objects.create(
                        smp_id=SMP_object, sub_heading="Exercises", sub_des=des)
                    SMP_des_object.save()

            for i in range(smp_form.cleaned_data["prerequisite_freq"]):
                des = smp_form.cleaned_data["Prerequisite_"+str(i+1)]
                if des:
                    SMP_des_object = SMP_des.objects.create(
                        smp_id=SMP_object, sub_heading="Prerequisites", sub_des=des)
                    SMP_des_object.save()

            for i in range(smp_form.cleaned_data["course-content_freq"]):
                des = smp_form.cleaned_data["Course-content_"+str(i+1)]
                if des:
                    SMP_des_object = SMP_des.objects.create(
                        smp_id=SMP_object, sub_heading="Course-content", sub_des=des)
                    SMP_des_object.save()

            for i in range(smp_form.cleaned_data["week_freq"]):
                for j in range(smp_form.cleaned_data["week_"+str(i+1)+"_description_freq"]):
                    des = smp_form.cleaned_data["Week_" +
                                                str(i+1)+"_Description_"+str(j+1)]
                    if des:
                        SMP_des_object = SMP_des.objects.create(
                            smp_id=SMP_object, sub_heading="Week "+str(i+1), sub_des=des)
                        SMP_des_object.save()

            messages.success(request, "SMP created")
            return redirect('acm:home_page')
        if password_form.is_valid():
            # To be hidden somehow
            if password_form.cleaned_data["key"] == "PASSWORD":
                validated = 1
            else:
                messages.MessageFailure(request, 'Incorrect password')
    else:
        password_form = PasswordForm()
        smp_form = SMPForm()
    static_fields = ['Name', 'Mentors', 'Overview', 'Platform']
    context = {'password_form': password_form,
               'smp_form': smp_form,
               'validated': validated,
               'static_fields': static_fields,
               'range_of_8': [1, 2, 3, 4, 5, 6, 7, 8]}
    return render(request, 'smp_form.html', context)
