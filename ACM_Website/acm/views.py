from django.shortcuts import render
from .models import *
import json
from django.http import HttpResponse
from .forms import *
from django.contrib import messages
from django.shortcuts import redirect

def home_page(request):
    events = Events.objects.all()
    special_people = Special_people.objects.all()

    # opens the json file and saves the raw contents
    data = open('acm/static/acm/json/index.json').read()
    descriptions = json.loads(data)
    sigo = SIG.objects.all()
    context = {'events': events, 'special_people': special_people,
               'descriptions': descriptions, 'sigo': sigo }
    return render(request, 'acm/index.html', context)


def sig_page(request, sig_id):
    si = SIG.objects.filter(pk=sig_id)
    sig = si[0]
    sigo = SIG.objects.all()
    events = Events.objects.filter(sig_id=sig_id)
    projects = Projects.objects.filter(sig_id=sig_id)
    with open('acm/static/acm/json/yantras.json') as f:
        data2 = json.loads(f.read())
        data =''
        x=len(sigo)
        for i in range (x):
            if(data2[i]['id']==sig_id):
                data=data2[i]  
        context = {'sig': sig, 'events': events,
               'projects': projects, 'sigo': sigo , 'data':data}
    return render(request, 'acm/yantras.html', context)


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
            if password_form.cleaned_data["key"] == "PASSWORD":
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
            if password_form.cleaned_data["key"] == "PASSWORD":
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
            if password_form.cleaned_data["key"] == "PASSWORD":
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
            if password_form.cleaned_data['key']=="PASSWORD":
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

