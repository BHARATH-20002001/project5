from django.urls import path
from pakisthan.views import *
app_name = 'something'
urlpatterns = [
    path('khan/',khan,name='khan'),
    path('azam/',azam,name='azam'),
]
