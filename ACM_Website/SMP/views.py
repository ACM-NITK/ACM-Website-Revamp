from .models import *
from acm.models import *
from django.http import JsonResponse
import json
from .forms import *
from django.contrib.auth.hashers import make_password


def home(request, sig_id):
    sig = SIG.objects.filter(pk=sig_id).values('id', 'name')[0]
    sigo = list(SIG.objects.all().values('id', 'name'))
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
    smp = SMP.objects.filter(pk=smp_id).values('id', 'name')[0]
    smp_des = list(SMP_des.objects.filter(smp_id=smp_id).values('id', 'smp_id', 'sub_heading', 'sub_des'))
    context = {'smp': smp, 'smp_des': smp_des}
    return JsonResponse(context)


def new_smp(request):
    validated = 0
    static_fields = ['Name', 'Mentors', 'Overview', 'Platform']
    dynammic_fields = ['Exercise', 'Prerequisite', 'Course-content']
    if request.method == "POST":
        request_params = request.body.decode('utf-8')
        data = json.loads(request_params)
        password_form = PasswordForm(data)
        smp_form = SMPForm(data)
        if smp_form.is_valid():
            sig = smp_form.cleaned_data["SIG"]
            name = smp_form.cleaned_data["Name"]
            mentors = smp_form.cleaned_data["Mentors"]
            overview = smp_form.cleaned_data["Overview"]
            platform = smp_form.cleaned_data["Platform"]
            SMP_object = SMP.objects.create(
                sig_id=SIG.objects.get(pk=sig), name=name,
                mentors=mentors, overview=overview, platform_of_tutoring=platform)
            SMP_object.save()

            for field in dynammic_fields:
                for i in range(smp_form.cleaned_data[field.lower() + "_freq"]):
                    des = smp_form.cleaned_data[field+'_' + str(i+1)]
                    if des:
                        SMP_des_object = SMP_des.objects.create(
                            smp_id=SMP_object, sub_heading=field, sub_des=des)
                        SMP_des_object.save()

            for i in range(smp_form.cleaned_data["week_freq"]):
                for j in range(smp_form.cleaned_data["week_"+str(i+1)+"_description_freq"]):
                    des = smp_form.cleaned_data["Week_" +
                                                str(i+1)+"_Description_"+str(j+1)]
                    if des:
                        SMP_des_object = SMP_des.objects.create(
                            smp_id=SMP_object, sub_heading="Week "+str(i+1), sub_des=des)
                        SMP_des_object.save()
            return JsonResponse({'message': 'SMP successfully created'}, status=201)

        if password_form.is_valid():
            # TODO: Use ENV variable to store PASSWORD
            if make_password(password_form.cleaned_data["key"]) == make_password("PASSWORD"):
                validated = 1
            else:
                JsonResponse({'message': 'Incorrect password'}, status=401)

    sigo = list(SIG.objects.all().values('id', 'name'))
    context = {'validated': validated,
               'static_fields': static_fields,
               'dynammic_fields': dynammic_fields,
               'range_of_8': [1, 2, 3, 4, 5, 6, 7, 8],
               'sigo': sigo, }

    return JsonResponse(context)
