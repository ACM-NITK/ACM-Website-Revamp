from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
import os

from .models import *
from SMP.models import *
import json
from django.http import JsonResponse
from .forms import *


def home_page(request):
    events = list(Events.objects.all().values('id', 'sig_id', 'name', 'description'))
    special_people = list(
        Special_people.objects.all().values('id', 'name', 'post', 'email_link', 'linkedin_link', 'image_path'))

    # opens the json file and saves the raw contents
    sigo = all_sigs()
    context = {'events': events, 'special_people': special_people, 'sigo': sigo}
    return JsonResponse(context)


def load_sig_contents(sig_id):
    sig = SIG.objects.filter(pk=sig_id).values('id', 'name', 'image', 'mission_statement', 'vision_statement')[0]
    sigo = all_sigs()
    events = list(Events.objects.filter(sig_id=sig_id).values('id', 'sig_id', 'name', 'description'))
    projects = list(Projects.objects.filter(sig_id=sig_id)
                    .values('id', 'name', 'display_picture', 'duration_in_months', 'mentors',
                            'members', 'introduction', 'method', 'results', 'obstacles',
                            'conclusion', 'future_work', 'references', 'meet_link'))
    with open('staticfiles/acm/json/yantras.json') as f:
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


def expo_index(request):
    context = {'sigo': all_sigs()}
    return JsonResponse(context)


def expo_year_wise(request, sig_id, year):
    sig, _, projects, sigo, data = load_sig_contents(sig_id)
    projects = projects.filter(year=year)
    context = {'projects': projects,
               'sigo': sigo,
               'sig': sig}

    return JsonResponse(context)


def expo(request, sig_id):
    return expo_year_wise(request, sig_id, 2020)


def project(request, project_id):
    context = {'project': Projects.objects.filter(id=project_id)
        .values('id', 'name', 'display_picture', 'duration_in_months', 'mentors',
                'members', 'introduction', 'method', 'results', 'obstacles',
                'conclusion', 'future_work', 'references', 'meet_link')[0],
               'sigo': all_sigs(),
               'pictures': list(ProjectPictures.objects.filter(project_id=project_id)
                                .values('id', 'project_id', 'picture', 'title'))}
    return JsonResponse(context)


def proposal_index(request):
    context = {'sigo': all_sigs()}
    return JsonResponse(context)


def all_proposals(request, sig_id):
    context = {'projects': list(Proposals.objects.filter(sig_id=sig_id)
                                .values('id', 'sig_id', 'name', 'duration_in_months', 'mentors', 'introduction',
                                        'method', 'existing_work', 'application', 'references', 'learning_outcomes',
                                        'results', 'image')),
               'sigo': all_sigs(),
               'sig':
                   SIG.objects.filter(id=sig_id).values('id', 'name', 'image', 'mission_statement', 'vision_statement')[
                       0]
               }

    return JsonResponse(context)


def proposal(request, proposal_id):
    context = {'project': Proposals.objects.filter(id=proposal_id)
        .values('id', 'sig_id', 'name', 'duration_in_months', 'mentors', 'introduction',
                'method', 'existing_work', 'application', 'references', 'learning_outcomes', 'results', 'image')[0],
               'sigo': all_sigs(),
               'timelines': list(ProposalTimeline.objects.filter(proposal_id=proposal_id)
                                 .values('id', 'proposal_id', 'phase', 'tasks', 'start_date', 'end_date'))
               }

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
            if make_password(password_form.cleaned_data["key"]) == make_password(os.environ["PASSWORD"]):
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
    sigo = all_sigs()
    context = {'sigo': sigo, 'valid': valid}
    return JsonResponse(context)


def contact_us(request):
    sigo = all_sigs()
    context = {'sigo': sigo}
    return JsonResponse(context)


def esp(request):
    sigo = all_sigs()
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
            return JsonResponse({'message': 'Project successfully added'}, status=201)
        if password_form.is_valid():
            if make_password(password_form.cleaned_data["key"]) == make_password(os.environ["PASSWORD"]):
                valid = 1
            else:
                return JsonResponse({'message': 'Incorrect Password'}, status=401)
    sigo = all_sigs()
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
            return JsonResponse({'message': 'Event successfully added'}, status=201)
        if password_form.is_valid():
            if make_password(password_form.cleaned_data["key"]) == make_password(os.environ["PASSWORD"]):
                valid = 1
            else:
                return JsonResponse({'message': 'Incorrect Password'}, status=401)
    sigo = all_sigs()
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
            return JsonResponse({'message': 'Event successfully updated'}, status=201)
        if password_form.is_valid():
            if make_password(password_form.cleaned_data["key"]) == make_password(os.environ["PASSWORD"]):
                valid = 1
            else:
                return JsonResponse({'message': 'Incorrect Password'}, status=401)
    sigo = all_sigs()
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
            return JsonResponse({'message': 'Project successfully updated'})
        if password_form.is_valid():
            if make_password(password_form.cleaned_data["key"]) == make_password(os.environ["PASSWORD"]):
                valid = 1
            else:
                return JsonResponse({'message': 'Incorrect Password'}, status=401)
    sigo = all_sigs()
    project = Projects.objects.get(pk=project_id)
    s = [project.id, project.sig_id.id, project.name, project.description, project.report_link, project.poster_link]
    context = {
        'sigo': sigo,
        'valid': valid,
        's': s,
    }
    return JsonResponse(context)


def club_events(request):
    context = {'events': list(Events.objects.filter(sig_id=None).values('id', 'name', 'description', 'image'))}
    return JsonResponse(context)


# Common block
def all_sigs():
    return list(SIG.objects.all().values('id', 'name', 'image', 'mission_statement', 'vision_statement'))
