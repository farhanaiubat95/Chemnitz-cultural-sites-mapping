from django.contrib import admin
from .models import BusParking
from .models import MotorhomeParking
from .models import CulturalSite

# Register your models here.

admin.site.register(BusParking) # Registering the BusParking model with the Django admin site
admin.site.register(MotorhomeParking) # Registering the MotorhomeParking models with the Django admin site
admin.site.register(CulturalSite) # Registering the CulturalSite model with the Django admin site