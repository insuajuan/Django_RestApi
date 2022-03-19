from django.urls import path
from . import views

# basic url: localhost/8000/api

urlpatterns = [
    path('', views.api_home)
]