from django.urls import path
from .views import AnneeUniversitaireListCreateView,AnneeUniversitaireDetailView

urlpatterns = [
    path('', AnneeUniversitaireListCreateView.as_view(), name='annee-universitaire-list'),
    path('<int:pk>/', AnneeUniversitaireDetailView.as_view(), name='annee-universitaire-detail'),
]