from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from annuaire.views import add_company, company_list, home, CompanyDeleteView,company_update,add_note, annonces

urlpatterns = [
    path('', home, name='index'),
    path('add/', add_company, name='add_company'),
    path('companies/', company_list, name='company_list'),
    path('company/<int:pk>/delete/', CompanyDeleteView.as_view(), name='company_delete'),
    path('companies/<int:pk>/update/', company_update, name='company_update'),
    path('companies/<int:company_id>/add_note/', add_note, name='add_note'),
    path('annonces/', annonces, name='annonces'),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
