from django.db import models
from pgvector.django import VectorField

class Etudiant(models.Model):
        nom = models.CharField(max_length=255)
        prenom=models.CharField(null=True,blank=True,max_length=255)
        embedding = VectorField(dimensions=528)
        matricule = models.CharField(null=True,max_length=15)
        genre = models.CharField(default='H',max_length=2)

