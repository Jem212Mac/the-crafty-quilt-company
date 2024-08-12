from django.urls import path
from . import views

""" urls for the contact form """

urlpatterns = [
    path('', views.contact, name='contact'),
]
