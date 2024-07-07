from django.contrib import admin
from .models import RentAdvertisement,RentRequest,Favourite,Review
from rest_framework.response import Response
# Register your models here.

class RentAdvertisementAdmin(admin.ModelAdmin):
   def save_model(self, request,obj,form,chnage) -> None:
    
    obj.save()
    obj.is_approved=True
    obj.save()

admin.site.register(RentAdvertisement,RentAdvertisementAdmin)

class RentRequestAdmin(admin.ModelAdmin):
   def save_model(self, request,obj,form,chnage) -> None:
    
    obj.save()
    if  obj.advertisement.request_accepted:
      obj.is_accepted = False
      obj.save()
      obj.advertisement.request_accepted = False
      obj.advertisement.save()
    else:
      obj.is_accepted = True
      obj.save()
      obj.advertisement.request_accepted = True
      obj.advertisement.save()

admin.site.register(RentRequest,RentRequestAdmin)
admin.site.register(Favourite)
admin.site.register(Review)
