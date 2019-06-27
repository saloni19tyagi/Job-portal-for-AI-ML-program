from django.shortcuts import render,redirect
from jobopening.models import JobOpening
from django.http import HttpResponse


def jobopening(request):
    if request.method == 'POST':
        job_opening = JobOpening()
        job_opening.company_name = request.POST['company_name']
        job_opening.position=request.POST['position']
        job_opening.experience=request.POST['experience']
        job_opening.salary = request.POST['salary']
        job_opening.skillsrequired = request.POST['skillsrequired']
        job_opening.save()
        return render(request, 'jobopening/vacancy_details.html')
    else:
        return render(request, 'jobopening/vacancy_details.html')


def home(request):
    if "id" not in request.GET:
        k = JobOpening.objects.filter(isActive=1)
        return render(request,"jobopening/home.html",{'post_list': k})
    else:
        id1 = int(request.GET.get('id'))
        k = JobOpening.objects.filter(id = id1)
        return render(request,'jobopening/details.html',{'detailing' : k})


def store_applications(request):
    if request.method == "POST":
        print("ndvhb")
        return render(request,'jobopening/vacancy_details.html')