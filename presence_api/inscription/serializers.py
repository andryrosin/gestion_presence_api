from rest_framework import serializers
from .models import Inscription
from etudiant.models import Etudiant


class InscriptionDirectSerializer(serializers.ModelSerializer):

    nom = serializers.CharField()
    prenom = serializers.CharField(required=False, allow_blank=True)
    matricule = serializers.CharField(required=False, allow_blank=True)
    genre = serializers.CharField()

    class Meta:
        model = Inscription
        fields = [
            'id',
            'nom',
            'prenom', 
            'matricule', 
            'genre',
            'niveau', 
            'annee', 
            'created'
        ]
        read_only_fields = ['created']

    def create(self, validated_data):
        # Extraire les données de l'étudiant
        nom = validated_data.pop('nom')
        prenom = validated_data.pop('prenom', None)
        matricule = validated_data.pop('matricule', None)
        genre = validated_data.pop('genre')

        # Créer l'étudiant
        etudiant = Etudiant.objects.create(
            nom=nom,
            prenom=prenom,
            matricule=matricule,
            genre=genre,
            embedding=None  # ou une valeur vide si pas encore généré
        )

        # Créer l’inscription
        inscription = Inscription.objects.create(
            etudiant=etudiant,
            **validated_data
        )

        return inscription
