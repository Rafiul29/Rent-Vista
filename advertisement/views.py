from django.shortcuts import render
from rest_framework import viewsets
from .models import RentAdvertisement
from .serializers import RentAdvertisementSerializer
# Create your views here.

class RentAdvertisementViewSet(viewsets.ModelViewSet):
  queryset=RentAdvertisement.objects.all()
  serializer_class=RentAdvertisementSerializer
  def get_queryset(self):
    queryset = super().get_queryset()
    user = self.request.user
    if user.is_staff:
      return queryset
    else:
      return queryset.filter(is_approved=True)