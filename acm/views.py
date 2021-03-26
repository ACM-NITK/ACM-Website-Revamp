from django.shortcuts import render
from .models import *
from SMP.models import *
import json
from django.http import HttpResponse
from .forms import *
from django.contrib import messages
from django.shortcuts import redirect

def home_page(request):
    events = Events.objects.all()
    special_people = Special_people.objects.all()

    # opens the json file and saves the raw contents
    data = open('staticfiles/acm/json/index.json',encoding='utf-8').read()
    descriptions = json.loads(data)
    sigo = SIG.objects.all()
    context = {'events': events,'sigo': sigo, 'descriptions':descriptions,'special_people':special_people}
    return render(request, 'acm/index.html', context)


def load_sig_contents(sig_id):
    si = SIG.objects.filter(pk=sig_id)
    sig = si[0]
    sigo = SIG.objects.all()
    events = Events.objects.filter(sig_id=sig_id)
    projects = Projects.objects.filter(sig_id=sig_id)
    with open('staticfiles/acm/json/yantras.json') as f:
        data2 = json.loads(f.read())
        data =''
        x=len(sigo)
        for i in range (x):
            if(data2[i]['id']==sig_id):
                data=data2[i]
    return sig, events, projects, sigo, data

def sig_page(request, sig_id):
    sig, events, _, sigo, data = load_sig_contents(sig_id)
    context = {'sig': sig, 'events': events, 'sigo': sigo , 'data':data}
    return render(request, 'acm/yantras.html', context)

def expo_index(request):
    context = {'sigo': SIG.objects.all()}
    return render(request, 'acm/expo_index.html', context)

def expo_year_wise(request, sig_id, year):
    sig, _, projects, sigo, data = load_sig_contents(sig_id)
    projects = projects.filter(year=year)
    context = {'projects': projects,
               'sigo': sigo,
                'sig': sig}

    return render(request, 'acm/expo.html', context)

def expo(request, sig_id):
    return expo_year_wise(request, sig_id, 2019)

def project(request, project_id):
    context = {'project': Projects.objects.get(id=project_id),
               'sigo': SIG.objects.all(),
               'pictures': ProjectPictures.objects.filter(project_id=project_id)}
    return render(request, 'acm/project.html', context)

def proposal_index(request):
    context = {'sigo': SIG.objects.all()}
    return render(request, 'acm/proposal_index.html', context)

def all_proposals(request, sig_id):
    context = {'projects': Proposals.objects.filter(sig_id = sig_id),
               'sigo': SIG.objects.all(),
               'sig': SIG.objects.get(id=sig_id)}

    return render(request, 'acm/all_proposals.html', context)

def proposal(request, proposal_id):
    print(proposal_id)
    context = {'project': Proposals.objects.get(id=proposal_id),
               'sigo': SIG.objects.all()}

    return render(request,'acm/proposal.html', context)

def manage(request, sig_id):
    sig, events, projects, sigo, data = load_sig_contents(sig_id)
    context = {'sig': sig, 'events': events,
               'projects': projects, 'sigo': sigo , 'data':data, 'smps':SMP.objects.filter(sig_id=sig_id)}
    return render(request, 'acm/manage.html', context)

def delete_component(request,type,id):
    valid=0
    if request.method == "POST":
        password_form=PasswordForm(request.POST)
        if password_form.is_valid():
            if password_form.cleaned_data["key"] == "s@ng@madethiz":
                valid = 1
                if type=="projects":
                    try:
                        Projects.objects.get(id=id).delete()
                        messages.success(request, "Project deleted")
                    except:
                        messages.MessageFailure(request, "Couldn't delete project")
                elif type=="events":
                    try:
                        Events.objects.get(id=id).delete()
                        messages.success(request, "Event deleted")
                    except:
                        messages.MessageFailure(request, "Couldn't delete event")
                elif type=="smp":
                    try:
                        SMP.objects.get(id=id).delete()
                        messages.success(request, "SMP deleted")
                    except:
                        messages.MessageFailure(request, "Couldn't delete SMP")
                
                return redirect('acm:home_page')
            else:
                messages.MessageFailure(request, 'Incorrect password')
        else:
            messages.MessageFailure(request, 'Incorrect password')
    else:
        password_form=PasswordForm()
    sigo = SIG.objects.all()
    context={ 'sigo':sigo, 'password_form':password_form ,'valid':valid }
    return render(request,'acm/projects_form.html',context)


def contact_us(request):
    sigo = SIG.objects.all()
    context = {'sigo': sigo}
    return render(request, 'acm/contact_us.html', context)


def esp(request):
    sigo = SIG.objects.all()
    context = {'sigo': sigo}
    return render(request, 'acm/esp.html', context)

def new_project(request):
    valid=0
    if request.method == "POST":
        project_form=Projectform(request.POST)
        password_form=PasswordForm(request.POST)
        if project_form.is_valid():
            sig=project_form.cleaned_data["SIG"]
            name=project_form.cleaned_data["Name"]
            des=project_form.cleaned_data["Description"]
            rep_link=project_form.cleaned_data["Report_link"]
            pos_link=project_form.cleaned_data["Poster_link"]
            project_obj=Projects.objects.create(sig_id=SIG.objects.get(pk=sig),name=name,description=des,report_link=rep_link,poster_link=pos_link)
            project_obj.save()
            messages.success(request, "Project successfully added")
            return redirect('/acm/')
        if password_form.is_valid():
            if password_form.cleaned_data["key"] == "s@ng@madethiz":
                valid = 1
            else:
                messages.MessageFailure(request, 'Incorrect password')   
    else :
        password_form=PasswordForm()
        project_form=Projectform()
    sigo = SIG.objects.all()
    context={ 'sigo':sigo, 'project_form':project_form, 'password_form':password_form ,'valid':valid }
    return render(request,'acm/projects_form.html',context)

def new_event(request):
    valid=0
    if request.method=="POST":
        event_form=EventsForm(request.POST)
        password_form=PasswordForm(request.POST)
        if event_form.is_valid():
            sig=event_form.cleaned_data["SIG"]
            name=event_form.cleaned_data["Name"]
            des=event_form.cleaned_data["Description"]
            event_obj=Events.objects.create(sig_id=SIG.objects.get(pk=sig),name=name,description=des)
            event_obj.save()
            messages.success(request, "Event successfully added")
            return redirect('/acm/')
        if password_form.is_valid():
            if password_form.cleaned_data["key"] == "s@ng@madethiz":
                valid = 1
            else:
                messages.MessageFailure(request, 'Incorrect password')
    else :
        password_form=PasswordForm()
        event_form=EventsForm()
    sigo = SIG.objects.all()
    context={ 'sigo':sigo, 'event_form':event_form, 'password_form':password_form ,'valid':valid }
    return render(request,'acm/event_form.html',context)


def update_event(request,event_id):
    valid=0
    if request.method=="POST":
        event_form=EventsForm(request.POST)
        password_form=PasswordForm(request.POST)
        if event_form.is_valid():
            sig=event_form.cleaned_data["SIG"]
            name=event_form.cleaned_data["Name"]
            des=event_form.cleaned_data["Description"]
            event_obj=Events.objects.create(sig_id=SIG.objects.get(pk=sig),name=name,description=des)
            event_obj.save()
            Events.objects.get(pk=event_id).delete()
            messages.success(request, "Event successfully added")
            return redirect('/acm/')
        if password_form.is_valid():
            if password_form.cleaned_data["key"] == "s@ng@madethiz":
                valid = 1
            else:
                messages.MessageFailure(request, 'Incorrect password')
    else :
        password_form=PasswordForm()
    sigo = SIG.objects.all()
    events = Events.objects.get(pk=event_id)
    s=[]
    s.append(events.name)
    s.append(events.description)
    event_form=EventsForm(initial={'SIG':events.sig_id})
    context={ 
              'sigo':sigo, 
              'event_form':event_form,
              'password_form':password_form ,
              'valid':valid,
              's':s,
             }
    return render(request,'acm/event_form.html',context)

def update_project(request,project_id):
    valid=0
    if request.method=="POST":
        project_form=Projectform(request.POST)
        password_form=PasswordForm(request.POST)
        if project_form.is_valid():
            sig=project_form.cleaned_data["SIG"]
            name=project_form.cleaned_data["Name"]
            des=project_form.cleaned_data["Description"]
            rep_link=project_form.cleaned_data["Report_link"]
            pos_link=project_form.cleaned_data["Poster_link"]
            project_obj=Projects.objects.create(sig_id=SIG.objects.get(pk=sig),name=name,description=des,report_link=rep_link,poster_link=pos_link)
            project_obj.save()
            Projects.objects.get(pk=project_id).delete()
            messages.success(request, "Project successfully added")
            return redirect('/acm/')
        if password_form.is_valid():
            if password_form.cleaned_data['key']=="s@ng@madethiz":
                valid=1
            else:
                messages.MessageFailure(request,'Incorrect password')
    else:
        password_form=PasswordForm()
    sigo=SIG.objects.all()
    project=Projects.objects.get(pk=project_id)
    s=[]
    s.append(project.name)
    s.append(project.description)
    s.append(project.report_link)
    s.append(project.poster_link)
    project_form=Projectform(initial={'SIG':project.sig_id})
    context={ 
              'sigo':sigo, 
              'project_form':project_form,
              'password_form':password_form ,
              'valid':valid,
              's':s,
             }
    return render(request,'acm/projects_form.html',context)

