from django import forms
from django.core.exceptions import ValidationError
from .models import Company, Note, JobAd, Document


class CompanyForm(forms.ModelForm):
    """
    Formulaire pour ajouter ou modifier une entreprise.
    """
    note = forms.CharField(max_length=500, required=False, label='Ajouter une note')

    class Meta:
        model = Company
        fields = (
            'name', 'website', 'email_address', 'physical_address', 'contact_name',
        )
        widgets = {
            'notes': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        }


class NoteForm(forms.ModelForm):
    """
    Formulaire pour ajouter une note à une entreprise.
    """
    class Meta:
        model = Note
        fields = ('text',)


class JobAdForm(forms.ModelForm):
    """
    Formulaire pour ajouter ou modifier une annonce.
    """

    class Meta:
        model = JobAd
        fields = ['company', 'job_title', 'job_description', 'job_location', 'job_type', 'job_link']
        widgets = {
            'job_type': forms.Select(attrs={'class': 'form-select'}),
        }
    def clean_company(self):
        """
        Vérifie si l'entreprise existe avant de l'associer à une annonce.
        """
        company = self.cleaned_data['company']
        if not Company.objects.filter(id=company.id).exists():
            raise ValidationError("L'entreprise n'existe pas. Veuillez d'abord créer l'entreprise.")
        return company


class DocumentForm(forms.ModelForm):
    """
    Formulaire pour ajouter un document à une annonce.
    """
    class Meta:
        model = Document
        fields = ['document']
