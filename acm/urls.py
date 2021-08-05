from django.urls import path
from .views import *

app_name = 'acm'
urlpatterns = [
    path('', home_page, name="home_page"),
    path('<int:sig_id>/', sig_page, name="sig_page"),
    path('contact_us/', contact_us),
    path('esp/', esp),
    path('<int:sig_id>/manage',manage),
    path('project/<int:project_id>', project),
    path('expo/<int:sig_id>', expo),
    path('expo/<int:sig_id>/<int:year>',expo_year_wise),
    path('expo', expo_index),
    path('proposal', proposal_index),
    path('all_proposals/<int:sig_id>', all_proposals),
    path('proposal/<int:proposal_id>', proposal),
    path('project/new',new_project),
    path('events/new',new_event),
    path('events/update/<int:event_id>/',update_event),
    path('projects/update/<int:project_id>/',update_project),
    path('<str:type>/delete/<int:id>/',delete_component),
    path('events/club_events', club_events)
]
