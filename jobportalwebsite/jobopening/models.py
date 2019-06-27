from django.db import models


class JobOpening(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=30)
    position = models.CharField(max_length=60)
    experience = models.CharField(max_length=60)
    salary = models.CharField(max_length=60)
    skillsrequired = models.TextField(max_length=60)
    isActive = models.BooleanField(default=False)

