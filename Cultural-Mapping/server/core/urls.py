from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BusParkingViewSet
from .views import MotorhomeParkingViewSet
from .views import CulturalSiteViewSet
from .views import AdministrativeDistrictViewSet
from .views import SaxonCulturalSiteViewSet

router = DefaultRouter()

# Register the viewsets with the router - BusParking and MotorhomeParking
router.register(r'bus-parkings', BusParkingViewSet, basename='busparking')
router.register(r'motorhome-parkings', MotorhomeParkingViewSet, basename='motorhomeparking')
router.register(r'cultural-sites', CulturalSiteViewSet, basename='culturalsite')
router.register(r'districts', AdministrativeDistrictViewSet, basename='district')
router.register(r'saxon-cultural-sites', SaxonCulturalSiteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
