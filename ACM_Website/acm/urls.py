from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page),
    path('<str:sig_name>/', sig_page),
]
