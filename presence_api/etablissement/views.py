from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Etablissement
from .serializers import EtablissementSerializer, CreateEtablissementSerializer
from allPermissions.permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated

class EtablissementListCreateView(generics.ListCreateAPIView):
    permission_classes=[IsAdmin]
    queryset = Etablissement.objects.all()
    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateEtablissementSerializer
        return EtablissementSerializer
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdmin()]
        return [IsAuthenticated()]
    def create(self, request, *args, **kwargs):
        create_serializer = self.get_serializer(data=request.data)
        create_serializer.is_valid(raise_exception=True)
        self.perform_create(create_serializer)
        instance = create_serializer.instance
        read_serializer = EtablissementSerializer(instance)
        headers = self.get_success_headers(read_serializer.data)
        return Response(read_serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class EtablissementDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAdmin]
    queryset = Etablissement.objects.all()
    serializer_class = EtablissementSerializer
