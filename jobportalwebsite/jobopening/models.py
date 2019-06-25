from django.db import models
from django.contrib.auth.models import User


class JobOpening(models.Model):
    company_name = models.CharField(max_length=30)
    position = models.CharField(max_length=60)
    experience = models.CharField(max_length=60)
    salary = models.CharField(max_length=60)
    skillsrequired = models.TextField(default="")
    isActive = models.BooleanField(default=False)
