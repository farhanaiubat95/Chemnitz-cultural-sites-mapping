from django.db import models
from django.contrib.gis.db import models
from django.contrib.postgres.fields import JSONField  

# Busparking model
class BusParking(models.Model):
    number = models.IntegerField()
    location = models.CharField(max_length=255)
    capacity = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    remarks = models.TextField(blank=True, null=True)
    x = models.FloatField()
    y = models.FloatField()
    point = models.PointField(geography=True, null=True)  # NEW

    def __str__(self):
        return f"{self.location} (No. {self.number})"


# MotorhomeParking model
class MotorhomeParking(models.Model):
    number = models.IntegerField()
    location = models.CharField(max_length=255)
    capacity = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    remarks = models.TextField(blank=True, null=True)
    x = models.FloatField()
    y = models.FloatField()
    point = models.PointField(geography=True, null=True)  # NEW

    def __str__(self):
        return f"{self.location} (No. {self.number})"


# CulturalSite model
class CulturalSite(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)  # Site name
    tourism = models.CharField(max_length=100, blank=True, null=True)  # e.g., 'museum'
    website = models.URLField(blank=True, null=True)  # URL to the official website
    operator = models.CharField(max_length=255, blank=True, null=True)  # Organization or company
    wheelchair_access = models.CharField(max_length=100, blank=True, null=True)  # e.g., 'yes', 'limited'
    osm_id = models.CharField(max_length=100, unique=True)  # '@id' field from GeoJSON
    location = models.PointField(geography=True)  # PostGIS spatial point

    def __str__(self):
        return self.name or self.osm_id #for avoiding duplicates from GeoJSON.


# AdministrativeDistrict model
class AdministrativeDistrict(models.Model):
    district_id = models.IntegerField()
    short_code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    kggs = models.CharField(max_length=20)
    area_km2 = models.FloatField()
    object_id = models.IntegerField()
    shape_area = models.FloatField()
    shape_length = models.FloatField()
    boundary = models.PolygonField(geography=True)

    def __str__(self):
        return self.name


# SaxonCulturalSite model
class SaxonCulturalSite(models.Model):
    osm_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    tourism = models.CharField(max_length=100, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    postcode = models.CharField(max_length=20, blank=True, null=True)
    building = models.CharField(max_length=100, blank=True, null=True)
    wheelchair = models.CharField(max_length=50, blank=True, null=True)
    wikidata = models.CharField(max_length=100, blank=True, null=True)
    geometry = models.GeometryField(geography=True)

    def __str__(self):
        return self.name or self.osm_id