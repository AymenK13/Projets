from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DeleteView
from .forms import CompanyForm, NoteForm
from .models import Company, JobAd
from django.urls import reverse_lazy
from .forms import DocumentForm
from django.db.models import Q


def add_company(request):
    """
    View pour ajouter une nouvelle entreprise à l'annuaire.

    Utilise un formulaire pour créer un nouvel objet Company dans la base de données.
    Si la requête est de type POST et que le formulaire est valide, l'entreprise est enregistrée dans la base de données
    et l'utilisateur est redirigé vers la page de liste des entreprises.

    Sinon, le formulaire vide est affiché.

    Args:
        request: La requête HTTP.

    Returns:
        La page HTML pour ajouter une entreprise.
    """
    template = 'add_company.html'

    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm()

    context = {
        'form': form,
    }

    return render(request, template, context)


def company_list(request):
    companies = Company.objects.all().order_by('-created_at')
    company_data = []

    for company in companies:
        documents = company.documents.filter(document__isnull=False)
        notes = company.notes.all()
        company_data.append({
            'company': company,
            'documents': documents,
            'notes': notes,
        })

    context = {'company_data': company_data}
    return render(request, 'company_list.html', context)


def home(request):
    """
    View pour afficher la page d'accueil.

    Args:
        request: La requête HTTP.

    Returns:
        La page HTML de la page d'accueil.
    """
    companies_count = Company.objects.count()
    job_ads_count = JobAd.objects.count()
    applications_count = JobAd.objects.filter(contact_date__isnull=False).count()
    latest_company = Company.objects.order_by('-created_at').first()
    latest_job_ad = JobAd.objects.latest('date_added') if job_ads_count > 0 else None

    context = {
        'companies_count': companies_count,
        'job_ads_count': job_ads_count,
        'applications_count': applications_count,
        'latest_company': latest_company,
        'latest_job_ad': latest_job_ad,
    }

    return render(request, 'index.html', context)


class CompanyDeleteView(DeleteView):
    """View pour supprimer une entreprise.

    Affiche un formulaire pour confirmer la suppression d'une entreprise.
    Si le formulaire est valide, supprime l'entreprise de la base de données.

    Attributes:
        model: Le modèle d'entreprise utilisé par la vue.
        success_url: L'URL vers laquelle rediriger l'utilisateur après la suppression d'une entreprise.
    """
    model = Company
    template_name = 'company_confirm_delete.html'
    success_url = reverse_lazy('company_list')


def edit_company(request, pk):
    """
    View pour modifier une entreprise existante dans l'annuaire.

    Utilise un formulaire pré-rempli pour modifier un objet Company dans la base de données.
    Si la requête est de type POST et que le formulaire est valide, l'entreprise est enregistrée dans la base de données
    et l'utilisateur est redirigé vers la page de liste des entreprises.

    Sinon, le formulaire pré-rempli est affiché.

    Args:
        request: La requête HTTP.
        pk: La clé primaire de l'entreprise à modifier.

    Returns:
        La page HTML pour modifier une entreprise.
    """
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm(instance=company)

    context = {
        'form': form,
        'company': company,
    }

    return render(request, 'edit_company.html', context)


def add_note(request, company_id):
    """
    View pour ajouter une note à une entreprise.

    Utilise un formulaire pour créer un nouvel objet Note dans la base de données.
    Si la requête est de type POST et que le formulaire est valide, la note est enregistrée dans la base de données
    et est associée à l'entreprise correspondante.

    Args:
        request: La requête HTTP.
        company_id: L'ID de l'entreprise à laquelle ajouter une note.

    Returns:
        La page HTML pour ajouter une note à une entreprise.
    """
    if request.method == 'POST':
        note_form = NoteForm(request.POST)
        if note_form.is_valid():
            company = Company.objects.get(id=company_id)
            note = note_form.save(commit=False)
            note.company = company
            note.save()
            company.notes.add(note)
            return redirect('company_list')
    else:
        note_form = NoteForm()

    context = {
        'note_form': note_form,
    }

    return render(request, 'add_note.html', context)


def add_document(request, company_id):
    """
    View qui affiche le formulaire pour ajouter un document à une entreprise donnée
    et qui enregistre les données du formulaire si valide.
    """
    company = get_object_or_404(Company, id=company_id)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.company = company
            document.save()
            return redirect('company_list')
    else:
        form = DocumentForm()
    return render(request, 'annuaire/add_document.html', {'form': form, 'company': company})


def search(request):
    """
    View qui permet de chercher des entreprises et des annonces d'emploi en fonction d'une requête de recherche.
    """
    query = request.GET.get('q')

    companies = Company.objects.filter(
        Q(name__icontains=query) | Q(city__icontains=query)
    ).order_by('-created_at')

    job_ads = JobAd.objects.filter(
        Q(job_title__icontains=query) | Q(job_description__icontains=query) | Q(job_location__icontains=query)
    )

    context = {
        'companies': companies,
        'job_ads': job_ads,
        'query': query,
    }
    return render(request, 'search_results.html', context)


def company_detail(request, pk):
    company = get_object_or_404(Company, pk=pk)
    notes = company.notes.all()
    documents = company.documents.all()

    context = {
        'company': company,
        'notes': notes,
        'documents': documents,
    }
    return render(request, 'company_detail.html', context)