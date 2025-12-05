from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Parcours
from .serializers import ParcoursSerializer,CreateParcoursSerializer
from allPermissions.permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated

class ParcoursListCreateView(generics.ListCreateAPIView):
    permission_classes=[IsAdmin]
    queryset = Parcours.objects.all()
    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateParcoursSerializer
        return ParcoursSerializer
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdmin()]
        return [IsAuthenticated()]
    def create(self, request, *args, **kwargs):
        create_serializer = self.get_serializer(data=request.data)
        create_serializer.is_valid(raise_exception=True)
        self.perform_create(create_serializer)
        instance = create_serializer.instance
        read_serializer = ParcoursSerializer(instance)
        headers = self.get_success_headers(read_serializer.data)
        return Response(read_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ParcoursDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAdmin]
    queryset = Parcours.objects.all()
    serializer_class = ParcoursSerializer
