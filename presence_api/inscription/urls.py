from django.urls import path
from .views import InscriptionCreateAPIView,ReInscriptionCreateAPIView

urlpatterns = [
    path('inscriptions/', InscriptionCreateAPIView.as_view(), name='etudiant-inscription'),
    path('reinscriptions/', ReInscriptionCreateAPIView.as_view(), name='etudiant-reinscription'),
]