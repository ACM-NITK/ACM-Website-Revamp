from django.contrib import admin
from .models import *


# register all the models to view and edit it through admin-page
admin.site.register(SIG)
admin.site.register(Events)
admin.site.register(Projects)
admin.site.register(Special_people)
