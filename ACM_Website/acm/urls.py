from django.urls import path
from .views import *

app_name = 'acm'
urlpatterns = [
    path('', home_page, name="home_page"),
    path('<int:sig_id>/', sig_page, name="sig_page"),
    path('contact_us/', contact_us),
    path('esp/', esp),
]
