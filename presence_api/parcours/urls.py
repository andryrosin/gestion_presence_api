from django.urls import path
from .views import ParcoursListCreateView,ParcoursDetailView

urlpatterns = [
    path('', ParcoursListCreateView.as_view(), name='parcours-list'),
    path('<int:pk>/', ParcoursDetailView.as_view(), name='parcours-detail'),
]