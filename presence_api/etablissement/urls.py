from django.urls import path
from .views import EtablissementListCreateView,EtablissementDetailView

urlpatterns = [
    path('', EtablissementListCreateView.as_view(), name='etablissement-list'),
    path('<int:pk>/', EtablissementDetailView.as_view(), name='etablissement-detail'),
]