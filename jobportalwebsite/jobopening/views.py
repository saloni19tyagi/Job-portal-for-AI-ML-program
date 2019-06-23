from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from jobopening.models import JobOpening


def jobopening(request):
    if request.method == 'POST':
        job_opening = JobOpening()
        JobOpening.company_name = request.POST['company_name']
        JobOpening.position=request.POST['position']
        JobOpening.experience=request.POST['experience']
        job_opening.save()
        return render(request, 'jobopening/vacancy_details.html')
    else:
        return render(request, 'jobopening/vacancy_details.html')


