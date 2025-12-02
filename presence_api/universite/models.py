from django.db import models

class Universite(models.Model):
    code = models.CharField(max_length=15)
    designation = models.CharField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.designation

