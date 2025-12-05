from django.urls import path
from .views import UniversiteListCreateView,UniversiteDetailView

urlpatterns = [
    path('', UniversiteListCreateView.as_view(), name='university-list'),
    path('<int:pk>/', UniversiteDetailView.as_view(), name='university-detail'),
]