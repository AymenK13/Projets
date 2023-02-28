from django import forms
from .models import Company, Note


class CompanyForm(forms.ModelForm):
    notes = forms.ModelMultipleChoiceField(
        queryset=Note.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Company
        fields = (
            'name', 'website', 'email_address', 'physical_address', 'contact_name', 'job_listing_site', 'notes'
        )


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('text',)
