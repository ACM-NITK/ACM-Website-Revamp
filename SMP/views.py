from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from acm.models import *
from django.http import JsonResponse
import json
from .forms import *


def home(request, sig_id):
    sig = SIG.objects.filter(pk=sig_id).values('id', 'name', 'image', 'mission_statement', 'vision_statement')[0]
    sigo = all_sigs()
    smps = list(SMP
                .objects
                .filter(sig_id=sig_id).values('id', 'sig_id', 'name', 'mentors', 'overview', 'platform_of_tutoring'))
    with open('acm/static/acm/json/smp.json') as f:
        data2 = json.loads(f.read())
        data = ''
        for i in range(5):
            if int(data2[i]['id']) == sig_id:
                data = data2[i]
    context = {'sig': sig, 'sigo': sigo, 'smps': smps, 'data': data}
    return JsonResponse(context)


def des(request, sig_id, smp_id):
    smp = SMP.objects.filter(pk=smp_id).values('id', 'sig_id', 'name', 'mentors', 'overview', 'platform_of_tutoring')[0]
    smp_des = list(SMP_des.objects.filter(smp_id=smp_id).values('id', 'smp_id', 'sub_heading', 'sub_des'))
    context = {'smp': smp, 'smp_des': smp_des}
    return JsonResponse(context)


def new_smp(request):
    validated = 0
    static_fields = ['Name', 'Mentors', 'Overview', 'Platform']
    dynamic_fields = ['Exercise', 'Prerequisite', 'Course-content']
    if request.method == "POST":
        smp_form = SMPForm(request.POST)
        if smp_form.is_valid():
            sig = smp_form.cleaned_data["SIG"]
            name = smp_form.cleaned_data["Name"]
            mentors = smp_form.cleaned_data["Mentors"]
            overview = smp_form.cleaned_data["Overview"]
            platform = smp_form.cleaned_data["Platform"]
            SMP_object = SMP.objects.create(
                sig_id=SIG.objects.get(pk=sig), name=name, mentors=mentors, overview=overview,
                platform_of_tutoring=platform)
            SMP_object.save()

            for field in dynamic_fields:
                for i in range(smp_form.cleaned_data[field.lower() + "_freq"]):
                    des = smp_form.cleaned_data[field + '_' + str(i + 1)]
                    if des:
                        SMP_des_object = SMP_des.objects.create(
                            smp_id=SMP_object, sub_heading=field, sub_des=des)
                        SMP_des_object.save()

            for i in range(smp_form.cleaned_data["week_freq"]):
                for j in range(smp_form.cleaned_data["week_" + str(i + 1) + "_description_freq"]):
                    des = smp_form.cleaned_data["Week_" +
                                                str(i + 1) + "_Description_" + str(j + 1)]
                    if des:
                        SMP_des_object = SMP_des.objects.create(
                            smp_id=SMP_object, sub_heading="Week " + str(i + 1), sub_des=des)
                        SMP_des_object.save()

            messages.success(request, "SMP created")
            return redirect('acm:home_page')

    else:
        smp_form = SMPForm()

    sigo = SIG.objects.all()
    context = {'smp_form': smp_form,
               'validated': validated,
               'static_fields': static_fields,
               'dynamic_fields': dynamic_fields,
               'range_of_8': [1, 2, 3, 4, 5, 6, 7, 8],
               'sigo': sigo, }

    return render(request, 'smp_form.html', context)


# Common block
def all_sigs():
    return list(SIG.objects.all().values('id', 'name', 'image', 'mission_statement', 'vision_statement'))
