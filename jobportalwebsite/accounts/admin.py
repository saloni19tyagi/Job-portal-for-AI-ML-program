from django.contrib import admin

# Register your models here.
from accounts.models import Register ,Company

admin.site.register(Register)
admin.site.register(Company)

