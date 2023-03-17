from django.urls import path
from app2.views import *
app_name='app2'
urlpatterns=[
    path('eswar/',eswar,name='eswar'),
    path('laxman/',laxman,name='laxman'),
]