from django.shortcuts import render
from rest_framework import viewsets
from .models import RentAdvertisement,RentRequest,Favourite,Review
from .serializers import RentAdvertisementSerializer,RentRequestSerializer,FavouriteSerializer,ReviewSerializer

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

class RentRequestViewSet(viewsets.ModelViewSet):
  queryset=RentRequest.objects.all()
  serializer_class=RentRequestSerializer
  def get_queryset(self):
      queryset = super().get_queryset()
      user = self.request.user
      if user.is_staff:
        return queryset
      else:
        return queryset.filter(is_accepted=True)
      
class FavouriteViewSet(viewsets.ModelViewSet):
  queryset=Favourite.objects.all()
  serializer_class=FavouriteSerializer


class ReviewViewSet(viewsets.ModelViewSet):
  queryset=Review.objects.all()
  serializer_class=ReviewSerializer