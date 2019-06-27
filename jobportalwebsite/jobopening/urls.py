from django.urls import path, include
from . import views


urlpatterns = [
    path('jobopening', views.jobopening, name='jobopening'),
    path('home', views.home, name='home'),
    path('store_applications',views.store_applications,name='store_applications'),
]