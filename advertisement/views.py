from django.shortcuts import render
from rest_framework import viewsets,filters
from .models import RentAdvertisement,RentRequest,Favourite,Review
from .serializers import RentAdvertisementSerializer,RentRequestSerializer,FavouriteSerializer,ReviewSerializer


from rest_framework.permissions import IsAuthenticated


# Create your views here.

class RentAdvertisementOwner(filters.BaseFilterBackend):
   def filter_queryset(self,request,query_set,view):
    owner_id=request.query_params.get('owner_id')
    if owner_id:
      return query_set.filter(owner=owner_id)
    return query_set
         

class RentAdvertisementViewSet(viewsets.ModelViewSet):
  queryset=RentAdvertisement.objects.all()
  serializer_class=RentAdvertisementSerializer
  filter_backends=[filters.SearchFilter,RentAdvertisementOwner]
  search_fields = ['category__name']

  def get_queryset(self):
    queryset = super().get_queryset()
    user = self.request.user
    if user.is_staff:
      return queryset
    else:
      return queryset.filter(is_approved=True)

class RentRequestSpecificAdvertisement(filters.BaseFilterBackend):
   def filter_queryset(self,request,query_set,view):
    requester_id=request.query_params.get('requester_id')
    if requester_id:
      return query_set.filter(requester=requester_id)
    return query_set
         

class RentRequestViewSet(viewsets.ModelViewSet):
  permission_classes=[IsAuthenticated]
  queryset=RentRequest.objects.all()
  serializer_class=RentRequestSerializer
  filter_backends=[RentRequestSpecificAdvertisement]
  def get_queryset(self):
      queryset = super().get_queryset()
      user = self.request.user
      if user.is_staff:
        return queryset
      else:
        return queryset.filter(is_accepted=True)

class FavouriteSpecificAdvertisement(filters.BaseFilterBackend):
   def filter_queryset(self,request,query_set,view):
    user_id=request.query_params.get('user_id')
    if user_id:
      return query_set.filter(user=user_id)
    return query_set
         
class FavouriteViewSet(viewsets.ModelViewSet):
  permission_classes=[IsAuthenticated]
  queryset=Favourite.objects.all()
  serializer_class=FavouriteSerializer
  filter_backends=[FavouriteSpecificAdvertisement]


class ReviewForSpecificAdvertisement(filters.BaseFilterBackend):
   def filter_queryset(self,request,query_set,view):
    advertisement_id=request.query_params.get('advertisement_id')
    if advertisement_id:
      return query_set.filter(advertisement=advertisement_id)
    return query_set

class ReviewViewSet(viewsets.ModelViewSet):
  # permission_classes=[IsAuthenticated]
  queryset=Review.objects.all()
  serializer_class=ReviewSerializer
  filter_backends=[ReviewForSpecificAdvertisement]
