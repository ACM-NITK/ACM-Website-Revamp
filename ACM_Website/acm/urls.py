from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page),
    path('<int:sig_id>/', sig_page),
    path('contact_us/', contact_us),
    path('esp/', esp),
]
