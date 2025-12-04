from django.db import models
from etablissement.models import Etablissement

class Mention(models.Model):
    code = models.CharField(max_length=15)
    designation = models.CharField()
    created = models.DateField(auto_now_add=True)
    etablissement = models.ForeignKey(
        Etablissement,
        on_delete=models.CASCADE,
        related_name="mentions",
        null=True
    )

    def __str__(self):
        return self.designation
