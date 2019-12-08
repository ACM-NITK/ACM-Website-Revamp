from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page),
    path('<int:sig_id>/', sig_page),
]
