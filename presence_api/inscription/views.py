from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Inscription
from .serializers import InscriptionDirectSerializer
from rest_framework.permissions import AllowAny

class InscriptionCreateAPIView(generics.CreateAPIView):
    permission_classes=[AllowAny]
    queryset = Inscription.objects.all()
    serializer_class = InscriptionDirectSerializer
    parser_classes = [MultiPartParser, FormParser]
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        inscription = serializer.save()
        return Response(
            self.get_serializer(inscription).data,
            status=status.HTTP_201_CREATED
        )
