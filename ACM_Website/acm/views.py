from django.shortcuts import render
from .models import *
import json


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
    context = {'sig': sig, 'events': events,
               'projects': projects, 'sigo': sigo}
    return render(request, 'acm/yantras.html', context)


def contact_us(request):
    sigo = SIG.objects.all()
    context = {'sigo': sigo}
    return render(request, 'acm/contact_us.html', context)


def esp(request):
    sigo = SIG.objects.all()
    context = {'sigo': sigo}
    return render(request, 'acm/esp.html', context)
