from django.db import models
from annee_universitaire.models import AnneeUniversitaire
from niveau.models import Niveau
from etudiant.models import Etudiant
class Inscription(models.Model):
    annee = models.ForeignKey(
        AnneeUniversitaire,
        on_delete=models.CASCADE,
        related_name="inscriptions"
    )
    niveau = models.ForeignKey(
        Niveau,
        on_delete=models.CASCADE,
        related_name="inscriptions"
    )
    etudiant = models.ForeignKey(
        Etudiant,
        on_delete=models.CASCADE,
        related_name="inscriptions",
        null=True
    )
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.etudiant.matricule}"