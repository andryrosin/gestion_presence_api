from rest_framework import serializers
from .models import AnneeUniversitaire

class AnneeUniversitaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnneeUniversitaire
        fields = ['id', 'annee','status']
