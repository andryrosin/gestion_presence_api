from rest_framework import serializers
from .models import Mention
from etablissement.serializers import EtablissementSerializer

class MentionSerializer(serializers.ModelSerializer):
    etablissement = EtablissementSerializer(read_only=True)
    class Meta:
        model = Mention
        fields = ['id', 'code','designation','etablissement']
class CreateMentionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mention
        fields = ['id', 'code','designation','etablissement']