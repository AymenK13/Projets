from django.db import models
from django.core.validators import EmailValidator

class Company(models.Model):
    """Modèle pour représenter une entreprise."""

    name = models.CharField(max_length=100, verbose_name="Nom de l'entreprise")
    website = models.URLField(blank=True, verbose_name="Site web de l'entreprise")
    email_address = models.EmailField(blank=True, null=True, verbose_name="Adresse email de l'entreprise", validators=[EmailValidator(message="L'adresse email n'est pas valide.")])
    physical_address = models.CharField(max_length=100, blank=True, verbose_name="Adresse physique de l'entreprise")
    contact_name = models.CharField(max_length=100, blank=True, verbose_name="Nom de la personne à contacter")
    job_listing_site = models.URLField(blank=True, verbose_name="Site web des offres d'emploi")
    notes = models.CharField(max_length=500, blank=True, verbose_name="Notes sur l'entreprise")  # champ de notes
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")


    def __str__(self):
        """Retourne une représentation en chaîne de caractères de l'objet Company."""
        return self.name


class Note(models.Model):
    """Modèle pour représenter une note."""

    text = models.TextField(verbose_name="Texte de la note")  # Texte de la note (obligatoire)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création de la note")  # Date de création de la note

    def __str__(self):
        """Retourne une représentation en chaîne de caractères de l'objet Note."""
        return self.text
