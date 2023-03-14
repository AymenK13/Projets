from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from annuaire.views_annuaire import add_company, company_list, home, CompanyDeleteView, edit_company, add_note
from annuaire.views_annonces import annonces, add_job_ad, delete_job_ad, update_contact_status, company_job_ads


urlpatterns = [
    path('', home, name='index'),
    path('add/', add_company, name='add_company'),
    path('companies/', company_list, name='company_list'),
    path('company/<int:pk>/delete/', CompanyDeleteView.as_view(), name='company_delete'),
    path('companies/<int:pk>/edit/', edit_company, name='edit_company'),
    path('companies/<int:company_id>/add_note/', add_note, name='add_note'),
    path('annonces/', annonces, name='annonces'),
    path('add_job_ad/', add_job_ad, name='add_job_ad'),
    path('annonces/<int:pk>/delete/', delete_job_ad, name='delete_job_ad'),
    path('update_contact_status/<int:pk>/', update_contact_status, name='update_contact_status'),
    path('companies/<int:company_id>/job-ads/', company_job_ads, name='company_job_ads'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
