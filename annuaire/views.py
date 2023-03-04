from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DeleteView
from .forms import CompanyForm, NoteForm
from .models import Company, JobPosting
from django.urls import reverse_lazy


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
    context = {'companies': companies}
    return render(request, 'company_list.html', context)


def home(request):
    """
    View pour afficher la page d'accueil.

    Args:
        request: La requête HTTP.

    Returns:
        La page HTML de la page d'accueil.
    """
    return render(request, 'index.html')


def add_note(request, company_id):
    company = Company.objects.get(id=company_id)

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            company.notes.add(note)
            return redirect('company_list')
    else:
        form = NoteForm()

    context = {
        'company': company,
        'form': form,
    }

    return render(request, 'add_note.html', context)


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


def company_update(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company_list')  # rediriger vers la vue company_detail
    else:
        form = CompanyForm(instance=company)
    return render(request, 'company_update.html', {'form': form, 'company': company})


def add_note(request, company_id):
    if request.method == 'POST':
        note_form = NoteForm(request.POST)
        if note_form.is_valid():
            company = Company.objects.get(id=company_id)
            note = note_form.save()
            company.notes.create(text=note.text)
            return redirect('company_list')
    else:
        note_form = NoteForm()

    context = {
        'note_form': note_form,
    }

    return render(request, 'add_note.html', context)


def annonces(request):
    return render(request, 'annonces.html')



def job_posting_list(request):
    job_postings = JobPosting.objects.all().order_by('-date_posted')
    context = {'job_postings': job_postings}
    return render(request, 'job_posting_list.html', context)