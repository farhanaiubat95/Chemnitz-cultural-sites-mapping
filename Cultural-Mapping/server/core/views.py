from rest_framework import viewsets
from .models import BusParking
from .serializers import BusParkingSerializer
from .models import MotorhomeParking
from .serializers import MotorhomeParkingSerializer

from .models import CulturalSite
from .serializers import CulturalSiteSerializer

from .models import AdministrativeDistrict
from .serializers import AdministrativeDistrictSerializer

from .models import SaxonCulturalSite
from .serializers import SaxonCulturalSiteSerializer

# Viewset for BusParking model
class BusParkingViewSet(viewsets.ModelViewSet):
    queryset = BusParking.objects.all()
    serializer_class = BusParkingSerializer


# Viewset for MotorhomeParking model
class MotorhomeParkingViewSet(viewsets.ModelViewSet):
    queryset = MotorhomeParking.objects.all()
    serializer_class = MotorhomeParkingSerializer



# Viewset for CulturalSite model
class CulturalSiteViewSet(viewsets.ModelViewSet):
    queryset = CulturalSite.objects.all()
    serializer_class = CulturalSiteSerializer


# Viewset for AdministrativeDistrict model
class AdministrativeDistrictViewSet(viewsets.ModelViewSet):
    queryset = AdministrativeDistrict.objects.all()
    serializer_class = AdministrativeDistrictSerializer



# Viewset for SaxonCulturalSiteViewSet model
class SaxonCulturalSiteViewSet(viewsets.ModelViewSet):
    queryset = SaxonCulturalSite.objects.all()
    serializer_class = SaxonCulturalSiteSerializer