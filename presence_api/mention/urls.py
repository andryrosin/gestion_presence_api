from django.urls import path
from .views import MentionListCreateView,MentionDetailView

urlpatterns = [
    path('', MentionListCreateView.as_view(), name='mention-list'),
    path('<int:pk>/', MentionDetailView.as_view(), name='mention-detail'),
]