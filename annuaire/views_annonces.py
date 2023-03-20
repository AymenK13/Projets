from django.shortcuts import render, redirect, get_object_or_404
from .models import JobAd, Company
from .forms import JobAdForm
from django.utils import timezone
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator


def annonces(request):
    """
    View qui affiche la liste de toutes les annonces d'emploi enregistrées,
    triées selon l'ordre spécifié par l'utilisateur et paginées.
    """
    sort_by = request.GET.get('sort_by')
    if not sort_by:
        sort_by = '-date_added'

    annonces_list = JobAd.objects.all().order_by(sort_by)

    paginator = Paginator(annonces_list, 6)
    page = request.GET.get('page')
    annonces = paginator.get_page(page)

    return render(request, 'job_ad_list.html', {'annonces': annonces, 'sort_by': sort_by})


def add_job_ad(request):
    """
    View qui affiche le formulaire pour ajouter une nouvelle annonce d'emploi
    et qui enregistre les données du formulaire si valide.
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
    View qui affiche la page de confirmation de suppression d'une annonce d'emploi
    et qui supprime l'annonce si l'utilisateur confirme.
    """
    job_ad = get_object_or_404(JobAd, pk=pk)
    if request.method == 'POST':
        job_ad.delete()
        return redirect('annonces')
    return render(request, 'delete_job_ad.html', {'job_ad': job_ad})


def update_contact_date(request, pk):
    """
    View qui met à jour la date de contact d'une annonce d'emploi
    et qui renvoie l'utilisateur à la liste des annonces d'emploi.
    """
    job_ad = get_object_or_404(JobAd, id=pk)
    contacted = request.POST.get('contacted', False)
    if contacted:
        contact_date = request.POST.get('contact_date', None)
        job_ad.contact_date = timezone.now()
        job_ad.save()
    return redirect('annonces')


def company_job_ads(request, company_id):
    """
    View qui récupère toutes les annonces d'une entreprise et les renvoie sous forme de contexte pour être affichées
    sur la page des annonces d'une entreprise.
    """
    company = get_object_or_404(Company, id=company_id)
    ad_count = company.job_ads.count()
    job_ads = JobAd.objects.filter(company=company)
    context = {'company': company, 'ad_count': ad_count, 'job_ads': job_ads}
    return render(request, 'company_job_ads.html', context)


def toggle_favorite(request, pk):
    """
    View qui permet de basculer l'état de l'annonce d'emploi entre favori et non favori
    et qui renvoie l'utilisateur à la liste des annonces d'emploi.
    """
    job_ad = get_object_or_404(JobAd, pk=pk)
    job_ad.is_favorite = not job_ad.is_favorite
    job_ad.save()
    return redirect(reverse('annonces'))


def check_company_existence(request):
    """
    Vérifie si l'entreprise saisie dans le formulaire d'ajout d'annonce existe déjà.
    Redirige vers la page d'ajout d'annonce si l'entreprise existe,
    ou vers la page d'ajout d'entreprise si elle n'existe pas.
    """
    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        try:
            company = Company.objects.get(name=company_name)
            return redirect('add_job_ad')
        except Company.DoesNotExist:
            messages.error(request, "L'entreprise n'existe pas. Veuillez d'abord créer l'entreprise.")
            return redirect('add_company')
    else:
        return render(request, 'check_company_existence.html')
