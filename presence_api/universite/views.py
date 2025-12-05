from rest_framework import generics
from .models import Universite
from .serializers import UniversiteSerializer
from allPermissions.permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated

class UniversiteListCreateView(generics.ListCreateAPIView):
    queryset = Universite.objects.all()
    serializer_class = UniversiteSerializer
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdmin()]
        return [IsAuthenticated()]

class UniversiteDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAdmin]
    queryset = Universite.objects.all()
    serializer_class = UniversiteSerializer
