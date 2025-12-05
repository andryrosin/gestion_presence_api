from django.urls import include, path
from .views import CustomTokenObtainPairView,UserRegistrationView,UsersListView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegistrationView.as_view(), name='user_register'),
    path('', UsersListView.as_view(), name='users_list'),
]