from rest_framework import generics
from .models import Niveau
from .serializers import NiveauSerializer
from allPermissions.permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated

class NiveauListCreateView(generics.ListCreateAPIView):
    queryset = Niveau.objects.all()
    serializer_class = NiveauSerializer
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdmin()]
        return [IsAuthenticated()]

class NiveauDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAdmin]
    queryset = Niveau.objects.all()
    serializer_class = NiveauSerializer
