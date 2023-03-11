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
        verbose_name="Name of the company"
    )
    website = models.URLField(
        blank=True,
        verbose_name="Website of the company"
    )
    city = models.CharField(
        max_length=100,
        default='Unknown',
        verbose_name="City of the company")

    email_address = models.EmailField(
        blank=True,
        null=True,
        verbose_name="Email address of the company",
        validators=[EmailValidator(message="The email address is not valid.")]
    )
    physical_address = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Physical address of the company"
    )
    contact_name = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Name of the contact person"
    )
    job_listing_site = models.URLField(
        blank=True,
        verbose_name="Job listing website"
    )
    notes = models.ManyToManyField(
        Note,
        blank=True,
        verbose_name="Notes about the company"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date of creation"
    )

    def __str__(self):
        return self.name

    def formatted_created_at(self):
        return timezone.localtime(self.created_at).strftime('%d/%m/%y %H:%M')


class JobAd(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )
    job_title = models.CharField(max_length=100)
    job_description = models.TextField()
    job_location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100)
    date_added = models.DateTimeField(default=timezone.now)
    is_favorite = models.BooleanField(default=False)
    job_link = models.CharField(max_length=255, default='')
    contact_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.job_title


