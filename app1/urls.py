from app1.views import *
from django.urls import path
app_name='something_is_fishy'
urlpatterns=[
    path('farha/',farha,name='farha'),
]