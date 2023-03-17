from django import forms
from django.core.exceptions import ValidationError
from .models import Company, Note, JobAd, Document


class CompanyForm(forms.ModelForm):
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
    class Meta:
        model = Note
        fields = ('text',)


class JobAdForm(forms.ModelForm):
    class Meta:
        model = JobAd
        fields = ['company', 'job_title', 'job_description', 'job_location', 'job_type', 'job_link']

    def clean_company(self):
        company = self.cleaned_data['company']
        if not Company.objects.filter(id=company.id).exists():
            raise ValidationError("L'entreprise n'existe pas. Veuillez d'abord créer l'entreprise.")
        return company


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['document']
