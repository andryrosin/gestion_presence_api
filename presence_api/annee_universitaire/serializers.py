from rest_framework import serializers
from .models import AnneeUniversitaire

class AnneeUniversiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnneeUniversitaire
        fields = ['id', 'annee','status']
