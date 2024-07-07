from django.contrib import admin
from .models import RentAdvertisement,RentRequest,Favourite,Review
# Register your models here.


admin.site.register(RentAdvertisement)
admin.site.register(RentRequest)
admin.site.register(Favourite)
admin.site.register(Review)
