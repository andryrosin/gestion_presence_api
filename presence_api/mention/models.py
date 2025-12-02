from django.db import models
from universite.models import Universite

class Mention(models.Model):
    universite = models.ForeignKey(
        Universite,
        on_delete=models.CASCADE,
        related_name="mentions"
    )
    code = models.CharField(max_length=15)
    designation = models.CharField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.designation
