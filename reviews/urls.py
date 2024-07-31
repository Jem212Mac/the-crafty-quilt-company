from django.urls import path
from . import views

urlpatterns = [
    path('', views.review, name='review'),
    path('<int:product_id>/', views.review, name='review'),
]