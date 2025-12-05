from django.urls import path
from .views import InscriptionCreateAPIView

urlpatterns = [
    path('inscriptions/', InscriptionCreateAPIView.as_view(), name='etudiant-inscription'),
]