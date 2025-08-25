from django.urls import path
from .views import (
    journalView,
    journalDetailView,
    journalCreateView,
    journalUpdateView,
    journalDeleteView
)

urlpatterns = [
    path('', journalView.as_view(), name='home'),
    path('journal/<int:pk>/', journalDetailView.as_view(), name='journal-detail'),
    path('journal/new/', journalCreateView.as_view(), name='journal-create'),
    path('journal/<int:pk>/edit/', journalUpdateView.as_view(), name='journal-update'),
    path('journal/<int:pk>/delete/', journalDeleteView.as_view(), name='journal-delete'),
]