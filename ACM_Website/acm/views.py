from django.shortcuts import render
from .models import *
from SMP.models import *
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import *
from django.contrib import messages
from django.shortcuts import redirect


def home_page(request):
    events = list(Events.objects.all().values('id', 'sig_id', 'name', 'description'))
    special_people = list(
        Special_people.objects.all().values('id', 'name', 'post', 'fb_link', 'linkedin_link', 'image_path'))

    # opens the json file and saves the raw contents
    sigo = list(SIG.objects.all().values('id', 'name'))
    context = {'events': events, 'special_people': special_people, 'sigo': sigo}
    return JsonResponse(context)


def load_sig_contents(sig_id):
    sig = SIG.objects.filter(pk=sig_id).values('id', 'name')[0]
    sigo = list(SIG.objects.all().values('id', 'name'))
    events = list(Events.objects.filter(sig_id=sig_id).values('id', 'sig_id', 'name', 'description'))
    projects = list(Projects.objects.filter(sig_id=sig_id).values('id', 'sig_id', 'name', 'description', 'report_link',
                                                                  'poster_link'))
    with open('/home/decoder/ACM-Website-Revamp/ACM_Website/staticfiles/acm/json/yantras.json') as f:
        data2 = json.loads(f.read())
        data = ''
        for i in range(len(sigo)):
            if data2[i]['id'] == sig_id:
                data = data2[i]
    return sig, events, projects, sigo, data


def sig_page(request, sig_id):
    sig, events, projects, sigo, data = load_sig_contents(sig_id)
    context = {'sig': sig, 'events': events,
               'projects': projects, 'sigo': sigo, 'data': data}
    return JsonResponse(context)


def manage(request, sig_id):
    sig, events, projects, sigo, data = load_sig_contents(sig_id)
    context = {'sig': sig, 'events': events,
               'projects': projects, 'sigo': sigo, 'data': data,
               'smps':
                   list(SMP.objects
                        .filter(sig_id=sig_id).values('id', 'sig_id', 'name', 'mentors', 'overview',
                                                      'platform_of_tutoring'))
               }
    return JsonResponse(context)


@csrf_exempt
def delete_component(request, type, id):
    valid = 0
    if request.method == "POST":
        request_params = request.body.decode('utf-8')
        data = json.loads(request_params)
        password_form = PasswordForm(data)
        if password_form.is_valid():
            if password_form.cleaned_data["key"] == "PASSWORD":
                valid = 1
                if type == "projects":
                    try:
                        Projects.objects.get(id=id).delete()
                        return JsonResponse({'message': 'Project successfully deleted'}, status=204)
                    except:
                        return JsonResponse({'message': "Couldn't delete project"}, status=422)
                elif type == "events":
                    try:
                        Events.objects.get(id=id).delete()
                        return JsonResponse({'message': 'Event successfully deleted'}, status=204)
                    except:
                        return JsonResponse({'message': "Couldn't delete event"}, status=422)
                elif type == "smp":
                    try:
                        SMP.objects.get(id=id).delete()
                        return JsonResponse({'message': 'SMP successfully deleted'}, status=204)
                    except:
                        return JsonResponse({'message': "Couldn't delete SMP"}, status=422)
            else:
                return JsonResponse({'message': 'Incorrect password'}, status=401)
        else:
            return JsonResponse({'message': 'Incorrect password'}, status=401)
    sigo = list(SIG.objects.all().values('id', 'name'))
    context = {'sigo': sigo, 'valid': valid}
    return JsonResponse(context)


def contact_us(request):
    sigo = list(SIG.objects.all().values('id', 'name'))
    context = {'sigo': sigo}
    return JsonResponse(context)


def esp(request):
    sigo = list(SIG.objects.all().values('id', 'name'))
    context = {'sigo': sigo}
    return JsonResponse(context)


@csrf_exempt
def new_project(request):
    valid = 0
    if request.method == "POST":
        request_params = request.body.decode('utf-8')
        data = json.loads(request_params)
        project_form = Projectform(data)
        password_form = PasswordForm(data)
        if project_form.is_valid():
            sig = project_form.cleaned_data["SIG"]
            name = project_form.cleaned_data["Name"]
            des = project_form.cleaned_data["Description"]
            rep_link = project_form.cleaned_data["Report_link"]
            pos_link = project_form.cleaned_data["Poster_link"]
            project_obj = Projects.objects.create(sig_id=SIG.objects.get(pk=sig), name=name, description=des,
                                                  report_link=rep_link, poster_link=pos_link)
            project_obj.save()
            # TODO: Check if redirect should be there (or) render a successful message
            return JsonResponse({'message': 'Project successfully added'}, status=201)
        # TODO: Check code logic
        if password_form.is_valid():
            if password_form.cleaned_data["key"] == "PASSWORD":
                valid = 1
            else:
                messages.MessageFailure(request, 'Incorrect password')
    sigo = list(SIG.objects.all().values('id', 'name'))
    context = {'sigo': sigo, 'valid': valid}
    return JsonResponse(context)


@csrf_exempt
def new_event(request):
    valid = 0
    if request.method == "POST":
        request_params = request.body.decode('utf-8')
        data = json.loads(request_params)
        event_form = EventsForm(data)
        password_form = PasswordForm(data)
        if event_form.is_valid():
            sig = event_form.cleaned_data["SIG"]
            name = event_form.cleaned_data["Name"]
            des = event_form.cleaned_data["Description"]
            event_obj = Events.objects.create(sig_id=SIG.objects.get(pk=sig), name=name, description=des)
            event_obj.save()
            # TODO: Check if redirect should be there (or) render a successful message
            return JsonResponse({'message': 'Event successfully added'}, status=201)
        # TODO: Check code logic
        if password_form.is_valid():
            if password_form.cleaned_data["key"] == "PASSWORD":
                valid = 1
            else:
                messages.MessageFailure(request, 'Incorrect password')
    sigo = list(SIG.objects.all().values('id', 'name'))
    context = {'sigo': sigo, 'valid': valid}
    return JsonResponse(context)


@csrf_exempt
def update_event(request, event_id):
    valid = 0
    if request.method == "POST":
        request_params = request.body.decode('utf-8')
        data = json.loads(request_params)
        event_form = EventsForm(data)
        password_form = PasswordForm(data)
        if event_form.is_valid():
            sig = event_form.cleaned_data["SIG"]
            name = event_form.cleaned_data["Name"]
            des = event_form.cleaned_data["Description"]
            Events.objects.filter(pk=event_id).update(sig_id=SIG.objects.get(pk=sig), name=name, description=des)
            # TODO: Check if redirect should be there (or) render a successful message
            return JsonResponse({'message': 'Event successfully updated'}, status=201)
        # TODO: Check code logic
        if password_form.is_valid():
            if password_form.cleaned_data["key"] == "PASSWORD":
                valid = 1
            else:
                messages.MessageFailure(request, 'Incorrect password')
    sigo = list(SIG.objects.all().values('id', 'name'))
    events = Events.objects.get(pk=event_id)
    s = [events.id, events.sig_id.id, events.name, events.description]
    context = {
        'sigo': sigo,
        'valid': valid,
        's': s,
    }
    return JsonResponse(context)


@csrf_exempt
def update_project(request, project_id):
    valid = 0
    if request.method == "POST":
        request_params = request.body.decode('utf-8')
        data = json.loads(request_params)
        project_form = Projectform(data)
        password_form = PasswordForm(data)
        if project_form.is_valid():
            sig = project_form.cleaned_data["SIG"]
            name = project_form.cleaned_data["Name"]
            des = project_form.cleaned_data["Description"]
            rep_link = project_form.cleaned_data["Report_link"]
            pos_link = project_form.cleaned_data["Poster_link"]
            Projects.objects.filter(pk=project_id).update(sig_id=SIG.objects.get(pk=sig), name=name, description=des,
                                                          report_link=rep_link, poster_link=pos_link)
            # TODO: Check if redirect should be there (or) render a successful message
            return JsonResponse({'message': 'Project successfully updated'})
        # TODO: Check code logic
        if password_form.is_valid():
            if password_form.cleaned_data['key'] == "PASSWORD":
                valid = 1
            else:
                messages.MessageFailure(request, 'Incorrect password')
    sigo = list(SIG.objects.all().values('id', 'name'))
    project = Projects.objects.get(pk=project_id)
    s = [project.id, project.sig_id.id, project.name, project.description, project.report_link, project.poster_link]
    context = {
        'sigo': sigo,
        'valid': valid,
        's': s,
    }
    return JsonResponse(context)
