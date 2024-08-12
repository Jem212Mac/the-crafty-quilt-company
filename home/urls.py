from django.urls import path
from . import views

""" urls for the home page """

urlpatterns = [
    path('', views.index, name='home')
]
