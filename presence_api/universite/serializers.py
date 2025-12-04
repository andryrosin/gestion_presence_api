from rest_framework import serializers
from .models import Universite

class UniversiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universite
        fields = ['id', 'code','designation']
