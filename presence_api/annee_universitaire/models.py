from django.db import models

class AnneeUniversitaire(models.Model):
    annee = models.CharField(max_length=15)
    status = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.annee
