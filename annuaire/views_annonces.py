from django.shortcuts import render
from .models import JobAd


def annonces(request):
    annonces = JobAd.objects.all()
    return render(request, 'job_ad_list.html', {'annonces': annonces})
