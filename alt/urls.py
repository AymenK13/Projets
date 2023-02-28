from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from annuaire.views import add_company, company_list, home, CompanyDeleteView

urlpatterns = [
    path('', home, name='index'),
    path('add/', add_company, name='add_company'),
    path('companies/', company_list, name='company_list'),
    path('company/<int:pk>/delete/', CompanyDeleteView.as_view(), name='company_delete'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
