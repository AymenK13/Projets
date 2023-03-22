# Generated by Django 4.1.7 on 2023-03-22 10:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('annuaire', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobad',
            options={'ordering': ['-date_added'], 'verbose_name': "Annonce d'emploi", 'verbose_name_plural': "Annonces d'emploi"},
        ),
        migrations.RemoveField(
            model_name='company',
            name='job_listing_site',
        ),
        migrations.AlterField(
            model_name='company',
            name='city',
            field=models.CharField(blank=True, default='Unknown', max_length=100, verbose_name="Ville de l'entreprise"),
        ),
        migrations.AlterField(
            model_name='company',
            name='contact_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Nom de la personne à contacter'),
        ),
        migrations.AlterField(
            model_name='company',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='company',
            name='email_address',
            field=models.EmailField(blank=True, max_length=254, null=True, validators=[django.core.validators.EmailValidator(message="L'adresse e-mail n'est pas valide.")], verbose_name="Adresse e-mail de l'entreprise"),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=100, verbose_name="Nom de l'entreprise"),
        ),
        migrations.AlterField(
            model_name='company',
            name='notes',
            field=models.ManyToManyField(blank=True, to='annuaire.note', verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='company',
            name='physical_address',
            field=models.CharField(blank=True, max_length=100, verbose_name="Adresse physique de l'entreprise"),
        ),
        migrations.AlterField(
            model_name='company',
            name='website',
            field=models.URLField(blank=True, verbose_name="Site web de l'entreprise"),
        ),
        migrations.AlterField(
            model_name='jobad',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_ads', to='annuaire.company', verbose_name='Entreprise'),
        ),
        migrations.AlterField(
            model_name='jobad',
            name='contact_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date de contact'),
        ),
        migrations.AlterField(
            model_name='jobad',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name="Date d'ajout"),
        ),
        migrations.AlterField(
            model_name='jobad',
            name='is_favorite',
            field=models.BooleanField(default=False, verbose_name='Favori'),
        ),
        migrations.AlterField(
            model_name='jobad',
            name='job_description',
            field=models.TextField(blank=True, verbose_name='Description du poste'),
        ),
        migrations.AlterField(
            model_name='jobad',
            name='job_link',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name="Lien vers l'annonce"),
        ),
        migrations.AlterField(
            model_name='jobad',
            name='job_location',
            field=models.CharField(blank=True, max_length=100, verbose_name='Lieu du poste'),
        ),
        migrations.AlterField(
            model_name='jobad',
            name='job_site',
            field=models.CharField(blank=True, max_length=100, verbose_name='Site du poste'),
        ),
        migrations.AlterField(
            model_name='jobad',
            name='job_title',
            field=models.CharField(max_length=100, verbose_name='Titre du poste'),
        ),
        migrations.AlterField(
            model_name='jobad',
            name='job_type',
            field=models.CharField(blank=True, choices=[('CDI', 'CDI'), ('CDD', 'CDD'), ('Alternance', 'Alternance'), ('Stage', 'Stage'), ('Freelance', 'Freelance')], max_length=100, verbose_name='Type de poste'),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='annuaire.company')),
            ],
        ),
    ]