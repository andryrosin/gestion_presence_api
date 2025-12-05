from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Mention
from .serializers import MentionSerializer, CreateMentionSerializer
from allPermissions.permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated

class MentionListCreateView(generics.ListCreateAPIView):
    permission_classes=[IsAdmin]
    queryset = Mention.objects.all()
    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateMentionSerializer
        return MentionSerializer
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdmin()]
        return [IsAuthenticated()]
    def create(self, request, *args, **kwargs):
        create_serializer = self.get_serializer(data=request.data)
        create_serializer.is_valid(raise_exception=True)
        self.perform_create(create_serializer)
        instance = create_serializer.instance
        read_serializer = MentionSerializer(instance)
        headers = self.get_success_headers(read_serializer.data)
        return Response(read_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class MentionDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAdmin]
    queryset = Mention.objects.all()
    serializer_class = MentionSerializer
