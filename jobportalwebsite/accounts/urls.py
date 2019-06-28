from django.urls import path,include
from accounts import views
# from django.contrib.auth import views as auth_views


urlpatterns = [

path('dashboard/',views.dashboard,name ='dashboard') ,
path('register/',  views.register,name='register'),
path('company/',  views.company,name='company'),
path('login/',views.login, name='login') ,
path('logout/', views.logout, name = 'logout') ,
]

