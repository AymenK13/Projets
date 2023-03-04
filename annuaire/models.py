from django.db import models
from django.core.validators import EmailValidator
from django.utils import timezone


class Note(models.Model):
    """Model for representing a note."""

    text = models.TextField(verbose_name="Text of the note")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date of creation of the note")

    def __str__(self):
        """Return a string representation of the Note object."""
        return self.text


class Company(models.Model):
    """Model for representing a company."""

    name = models.CharField(max_length=100, verbose_name="Name of the company")
    website = models.URLField(blank=True, verbose_name="Website of the company")
    email_address = models.EmailField(blank=True, null=True, verbose_name="Email address of the company", validators=[EmailValidator(message="The email address is not valid.")])
    physical_address = models.CharField(max_length=100, blank=True, verbose_name="Physical address of the company")
    contact_name = models.CharField(max_length=100, blank=True, verbose_name="Name of the contact person")
    job_listing_site = models.URLField(blank=True, verbose_name="Job listing website")
    notes = models.ManyToManyField(Note, blank=True, verbose_name="Notes about the company")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date of creation")

    def __str__(self):
        """Return a string representation of the Company object."""
        return self.name

    def formatted_created_at(self):
        """Return the formatted creation date of the Company object."""
        return timezone.localtime(self.created_at).strftime('%d/%m/%y %H:%M')


class JobPosting(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)