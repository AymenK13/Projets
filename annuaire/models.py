from django.core.validators import EmailValidator
from django.db import models
from django.utils import timezone


class Note(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class Company(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Nom de l'entreprise"
    )
    website = models.URLField(
        blank=True,
        verbose_name="Site web de l'entreprise"
    )
    city = models.CharField(
        max_length=100,
        default='Unknown',
        blank=True,
        verbose_name="Ville de l'entreprise")

    email_address = models.EmailField(
        blank=True,
        null=True,
        verbose_name="Adresse e-mail de l'entreprise",
        validators=[EmailValidator(message="L'adresse e-mail n'est pas valide.")]
    )
    physical_address = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Adresse physique de l'entreprise"
    )
    contact_name = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Nom de la personne à contacter"
    )
    notes = models.ManyToManyField(
        Note,
        blank=True,
        verbose_name="Notes"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date de création"
    )

    def __str__(self):
        return self.name

    def formatted_created_at(self):
        return timezone.localtime(self.created_at).strftime('%d/%m/%y %H:%M')

    def ad_count(self):
        return self.job_ads.count()


class JobAd(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='job_ads',
        verbose_name="Entreprise"
    )
    job_title = models.CharField(
        max_length=100,
        verbose_name="Titre du poste"
    )
    job_description = models.TextField(
        blank=True,
        verbose_name="Description du poste"
    )
    job_location = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Lieu du poste"
    )
    job_type = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Type de poste"
    )
    job_site = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Site du poste"
    )
    date_added = models.DateTimeField(
        default=timezone.now,
        verbose_name="Date d'ajout"
    )
    job_link = models.CharField(
        max_length=255,
        default='',
        blank=True,
        verbose_name="Lien vers l'annonce"
    )
    contact_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Date de contact"
    )
    is_favorite = models.BooleanField(
        default=False,
        verbose_name="Favori"
    )

    class Meta:
        ordering = ['-date_added']
        verbose_name = "Annonce d'emploi"
        verbose_name_plural = "Annonces d'emploi"

    def __str__(self):
        return self.job_title


class Document(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE,
        related_name='documents',
    )
    document = models.FileField(
        upload_to='documents/',
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.document.name} ({self.company.name})"

