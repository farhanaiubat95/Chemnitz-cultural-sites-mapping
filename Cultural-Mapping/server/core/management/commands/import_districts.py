import json
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import GEOSGeometry
from core.models import AdministrativeDistrict

class Command(BaseCommand):
    help = 'Import administrative districts from Stadtteile.geojson'

    def handle(self, *args, **kwargs):
        filepath = 'D:\Python\Cultural-Mapping\server\core\data\Stadtteile.geojson'

        with open(filepath, encoding='utf-8') as f:
            geojson = json.load(f)

        for feature in geojson['features']:
            props = feature['properties']
            geom = GEOSGeometry(json.dumps(feature['geometry']))

            # Create or update to avoid duplicates if rerun
            AdministrativeDistrict.objects.update_or_create(
                district_id=props.get('ID'),  # e.g. 35
                defaults={
                    'short_code': str(props.get('STADTTS')),  # e.g. "47"
                    'name': props.get('STADTTNAME'),           # e.g. "Klaffenbach"
                    'kggs': props.get('KGGS'),                  # e.g. "4700000"
                    'area_km2': float(props.get('FLAECHE')),    # e.g. 8
                    'object_id': props.get('OBJECTID'),         # e.g. 1
                    'shape_area': float(props.get('SHAPE__Area')),    # e.g. 21496768.479492188
                    'shape_length': float(props.get('SHAPE__Length')), # e.g. 25757.412047690304
                    'boundary': geom,
                }
            )

        self.stdout.write(self.style.SUCCESS('Administrative districts imported successfully.'))
