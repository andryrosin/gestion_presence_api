from rest_framework import serializers
from .models import Inscription
from etudiant.models import Etudiant
from detection.detection import FaceModel

model = FaceModel()

class InscriptionDirectSerializer(serializers.ModelSerializer):
    nom = serializers.CharField(write_only=True)
    prenom = serializers.CharField(required=False, allow_blank=True,write_only=True)
    matricule = serializers.CharField(required=False, allow_blank=True,write_only=True)
    genre = serializers.CharField(write_only=True)
    photo = serializers.ImageField(required=True,write_only=True)

    class Meta:
        model = Inscription
        fields = [
            'id',
            'nom', 
            'prenom', 
            'matricule', 
            'genre', 
            'photo',
            'niveau', 
            'annee',
            'created'
        ]
        read_only_fields = ['created']

    def create(self, validated_data):
        nom = validated_data.pop('nom')
        prenom = validated_data.pop('prenom', None)
        matricule = validated_data.pop('matricule', None)
        genre = validated_data.pop('genre')
        photo = validated_data.pop('photo')

        etudiant = Etudiant.objects.create(
            nom=nom,
            prenom=prenom,
            matricule=matricule,
            genre=genre,
            photo=photo
        )

        if etudiant.photo:
            emb,box = model.detect_face(etudiant.photo.path)
            if emb is not None:
                etudiant.embedding = emb
                etudiant.save()

        inscription = Inscription.objects.create(
            etudiant=etudiant,
            **validated_data
        )

        return inscription
