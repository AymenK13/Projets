from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DeleteView
from .forms import CompanyForm, NoteForm
from .models import Company, Note, Document
from django.urls import reverse_lazy
from .forms import DocumentForm


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
    return render(request, 'index.html')


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
            company.notes.add(note)  # Change this line
            return redirect('company_list')
    else:
        note_form = NoteForm()

    context = {
        'note_form': note_form,
    }

    return render(request, 'add_note.html', context)


def add_document(request, company_id):
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