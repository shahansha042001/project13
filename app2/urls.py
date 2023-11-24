from app2.views import *
from django.urls import path
app_name='ask_farha'
urlpatterns=[
    path('response/',response,name='response'),
]