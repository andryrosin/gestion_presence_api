from rest_framework import serializers
from .models import Parcours
from mention.serializers import MentionSerializer

class MentionSerializer(serializers.ModelSerializer):
    mention = MentionSerializer(read_only=True)
    class Meta:
        model = Parcours
        fields = ['id', 'code','designation','mention']
class CreateMentionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcours
        fields = ['id', 'code','designation','mention']