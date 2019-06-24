from django.urls import path, include
from . import views

urlpatterns = [
    path('home1/', views.home, name='home'),
]