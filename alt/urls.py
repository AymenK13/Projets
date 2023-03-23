from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from annuaire.views_annuaire import add_company, company_list, home, CompanyDeleteView, edit_company, add_note,     \
                                    add_document, search,company_detail
from annuaire.views_annonces import annonces, add_job_ad, delete_job_ad, update_contact_date, company_job_ads,  \
                                    toggle_favorite, check_company_existence


urlpatterns = [
    # Page d'accueil
    path('', home, name='index'),
    path('search/', search, name='search'),

    # Entreprises
    path('add/', add_company, name='add_company'),
    path('companies/', company_list, name='company_list'),
    path('company/<int:pk>/delete/', CompanyDeleteView.as_view(), name='company_delete'),
    path('companies/<int:pk>/edit/', edit_company, name='edit_company'),
    path('companies/<int:company_id>/add_note/', add_note, name='add_note'),
    path('companies/<int:company_id>/add_document/', add_document, name='add_document'),
    path('company/<int:pk>/', company_detail, name='company_detail'),


    # Annonces
    path('annonces/', annonces, name='annonces'),
    path('add_job_ad/', add_job_ad, name='add_job_ad'),
    path('annonces/<int:pk>/delete/', delete_job_ad, name='delete_job_ad'),
    path('update_contact_date/<int:pk>/', update_contact_date, name='update_contact_date'),
    path('companies/<int:company_id>/job-ads/', company_job_ads, name='company_job_ads'),
    path('toggle_favorite/<int:pk>/', toggle_favorite, name='toggle_favorite'),
    path('check_company_existence/', check_company_existence, name='check_company_existence'),

]

if settings.DEBUG:
    # Ajout des fichiers static en mode DEBUG
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

