from .models import Lead
from .serializers import LeadSerializer
from rest_framework import generics
from rest_framework import viewsets, permissions


class LeadListCreate(generics.ListCreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = LeadSerializer

    def get_queryset(self):
        return self.request.user.leads.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)