# Generated by Django 4.1.7 on 2023-02-22 19:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('website', models.URLField()),
                ('email_address', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator(message='Email is not valid.')])),
                ('physical_address', models.CharField(max_length=100)),
                ('contact_name', models.CharField(max_length=100)),
                ('job_listing_site', models.URLField()),
                ('notes', models.ManyToManyField(blank=True, to='annuaire.note')),
            ],
        ),
    ]
