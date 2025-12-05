from django.urls import path
from .views import NiveauListCreateView,NiveauDetailView

urlpatterns = [
    path('', NiveauListCreateView.as_view(), name='niveau-list'),
    path('<int:pk>/', NiveauDetailView.as_view(), name='niveau-detail'),
]