from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from .serializers import CustomUserSerializer, UserSerializer, UserListSerializer
from rest_framework.views import APIView
from allPermissions.permissions import IsAdmin
from django.db.models import Value, F
from django.db.models.functions import Concat

class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.user
            refresh = RefreshToken.for_user(user)
            access = str(refresh.access_token)
            refresh = str(refresh)
            user_data = CustomUserSerializer(user).data
            return Response({
                'refresh': refresh,
                'access': access,
                'user': user_data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UserRegistrationView(APIView):
    permission_classes = [IsAdmin]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  
            list_serializer = UserListSerializer(user) 
            return Response(list_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsersListView(generics.ListAPIView):
    permission_classes = [IsAdmin]
    queryset = User.objects.all().annotate(
        full_name=Concat(F('first_name'), Value(' '), F('last_name'))
    )
    serializer_class = UserListSerializer