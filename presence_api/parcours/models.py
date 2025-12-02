from django.db import models
from mention.models import Mention

class Parcours(models.Model):
    mention = models.ForeignKey(
        Mention,
        on_delete=models.CASCADE,
        related_name="parcours"
    )
    code = models.CharField(max_length=15)
    designation = models.CharField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.designation

