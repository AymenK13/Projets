from django.shortcuts import render, redirect, get_object_or_404
from .models import JobAd, Company
from .forms import JobAdForm


def annonces(request):
    """
    View qui récupère toutes les annonces et les renvoie sous forme de contexte
    pour être affichées sur la page des annonces
    """
    annonces = JobAd.objects.all()
    return render(request, 'job_ad_list.html', {'annonces': annonces})


def add_job_ad(request):
    """
    View qui affiche le formulaire pour ajouter une nouvelle annonce
    et qui enregistre les données du formulaire si valide
    """
    if request.method == 'POST':
        form = JobAdForm(request.POST)
        if form.is_valid():
            job_ad = form.save(commit=False)
            job_ad.save()
            return redirect('annonces')
    else:
        form = JobAdForm()
    return render(request, 'add_job_ad.html', {'form': form})


def delete_job_ad(request, pk):
    """
    View qui affiche la page de confirmation de suppression d'une annonce
    et qui supprime l'annonce si l'utilisateur confirme
    """
    job_ad = get_object_or_404(JobAd, pk=pk)
    if request.method == 'POST':
        job_ad.delete()
        return redirect('annonces')
    return render(request, 'delete_job_ad.html', {'job_ad': job_ad})


def update_contact_status(request, pk):
    """
    View qui met à jour le statut de contact d'une annonce
    """
    annonce = get_object_or_404(JobAd, pk=pk)
    if request.method == 'POST':
        contacted = request.POST.get('contacted', False)
        contact_date = request.POST.get('contact_date', None)
        annonce.contact_date = contact_date if contacted else None
        annonce.save()
        return redirect('annonces')
    else:
        return render(request, 'job_ad_list.html', {'annonces': JobAd.objects.all()})


def company_job_ads(request, company_id):
    """
    View qui récupère toutes les annonces d'une entreprise et les renvoie sous forme de contexte pour être affichées
    sur la page des annonces d'une entreprise
    """
    company = get_object_or_404(Company, id=company_id)
    ad_count = company.job_ads.count()
    job_ads = JobAd.objects.filter(company=company)
    context = {'company': company, 'ad_count': ad_count, 'job_ads': job_ads}
    return render(request, 'company_job_ads.html', context)
