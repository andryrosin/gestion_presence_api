from rest_framework import generics
from .models import AnneeUniversitaire
from .serializers import AnneeUniversitaireSerializer
from allPermissions.permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated

class AnneeUniversitaireListCreateView(generics.ListCreateAPIView):
    queryset = AnneeUniversitaire.objects.all()
    serializer_class = AnneeUniversitaireSerializer
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdmin()]
        return [IsAuthenticated()]

class AnneeUniversitaireDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAdmin]
    queryset = AnneeUniversitaire.objects.all()
    serializer_class = AnneeUniversitaireSerializer
