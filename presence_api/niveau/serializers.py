from rest_framework import serializers
from .models import Niveau

class NiveauSerializer(serializers.ModelSerializer):
    class Meta:
        model = Niveau
        fields = ['id', 'code','designation','hierarchie']
