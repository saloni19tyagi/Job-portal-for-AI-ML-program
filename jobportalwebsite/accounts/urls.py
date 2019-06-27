from django.urls import path,include
from accounts import views
# from django.contrib.auth import views as auth_views


urlpatterns = [

path('register/',  views.register,name='register'),
path('login/',views.login, name='login') ,
path('logout/', views.logout, name = 'logout') ,
# path('logout/',auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),

]

