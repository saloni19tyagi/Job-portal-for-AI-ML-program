from django.urls import path, include
from . import views

urlpatterns = [
    path('jobopening', views.jobopening, name='jobopening'),
]