from django.urls import path
from .views import *

app_name = 'acm'
urlpatterns = [
    path('', home_page, name="home_page"),
    path('<int:sig_id>/', sig_page, name="sig_page"),
    path('contact_us/', contact_us),
    path('esp/', esp),
    path('<int:sig_id>/manage',manage),
    path('project/new',new_project),
    path('events/new',new_event),
    path('events/update/<int:event_id>/',update_event),
    path('projects/update/<int:project_id>/',update_project),
    path('<str:type>/delete/<int:id>/',delete_component),
]
