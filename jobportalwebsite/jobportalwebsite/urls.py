from django.contrib import admin
from account import views
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    # path('account/',include('account.urls')),
    path('opening/',include('jobopening.urls')),
]

