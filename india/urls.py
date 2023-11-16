from django.urls import path
from india.views import *
app_name = 'something'

urlpatterns = [
    path('msd/',msd,name='msd'),
    path('jadeja/',jadeja,name='jadeja'),
]