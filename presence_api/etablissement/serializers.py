from rest_framework import serializers
from .models import Etablissement
from universite.serializers import UniversiteSerializer

class EtablissementSerializer(serializers.ModelSerializer):
    universite = UniversiteSerializer(read_only=True)
    class Meta:
        model = Etablissement
        fields = ['id', 'code','designation','universite']
class CreateEntiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etablissement
        fields = ['id', 'code','designation','universite']