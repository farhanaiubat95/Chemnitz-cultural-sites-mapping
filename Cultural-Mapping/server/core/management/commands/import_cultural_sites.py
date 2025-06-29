import json
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point
from core.models import CulturalSite

class Command(BaseCommand):
    help = 'Import cultural sites from GeoJSON file'

    def handle(self, *args, **options):
        path = r'D:\Python\Cultural-Mapping\server\core\data\Chemnitz.geojson'
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        count = 0
        for feature in data['features']:
            props = feature['properties']
            geom = feature['geometry']
            if geom['type'] != 'Point':
                continue

            lon, lat = geom['coordinates']
            site = CulturalSite(
                name=props.get('name', 'Unknown'),
                operator=props.get('operator'),
                website=props.get('website'),
                wheelchair_access=props.get('wheelchair'),
                tourism=props.get('tourism'),
                osm_id=feature.get('id'),
                location=Point(lon, lat)
            )
            site.save()
            count += 1

        self.stdout.write(self.style.SUCCESS(f'Imported {count} cultural sites'))
