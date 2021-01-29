from django.urls import path
from .views import *
app_name = 'SMP'
urlpatterns = [
    path('<int:sig_id>/', home),
    path('<int:sig_id>/<int:smp_id>/', des)
]
