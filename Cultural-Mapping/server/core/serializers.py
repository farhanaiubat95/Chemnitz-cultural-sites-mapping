from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import BusParking
from .models import MotorhomeParking
from .models import CulturalSite
from .models import AdministrativeDistrict
from .models import SaxonCulturalSite


# Serializer for BusParking model
class BusParkingSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = BusParking
        geo_field = "point"
        fields = "__all__"

# Serializer for MotorhomeParking model
class MotorhomeParkingSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = MotorhomeParking
        geo_field = "point"
        fields = "__all__"


# Serializer for CulturalSite model
class CulturalSiteSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = CulturalSite
        geo_field = "location"  # Must match your model's PointField name
        fields = ("id", "name", "tourism", "website", "operator", "wheelchair_access", "osm_id")


# Serializer for AdministrativeDistrict model
class AdministrativeDistrictSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = AdministrativeDistrict
        geo_field = "boundary"
        fields = (
            "id",             # Django default primary key
            "district_id",    # Custom ID from GeoJSON
            "short_code",     # STADTTS
            "name",           # STADTTNAME
            "kggs",           # KGGS
            "area_km2",       # FLAECHE
            "object_id",      # OBJECTID
            "shape_area",     # SHAPE__Area
            "shape_length"    # SHAPE__Length
        )

# Serializer for SaxonCulturalSite model
class SaxonCulturalSiteSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = SaxonCulturalSite
        geo_field = 'geometry'
        fields = '__all__'