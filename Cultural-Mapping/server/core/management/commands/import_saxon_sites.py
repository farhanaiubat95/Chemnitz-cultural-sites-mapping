import json
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import GEOSGeometry
from core.models import SaxonCulturalSite

class Command(BaseCommand):
    help = 'Import Saxon cultural sites from Sachsen.geojson'

    def handle(self, *args, **kwargs):
        path = r'D:\Python\Cultural-Mapping\server\core\data\Sachsen.geojson'
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        count = 0
        for feature in data['features']:
            props = feature['properties']
            geom = feature['geometry']

            geometry = GEOSGeometry(json.dumps(geom))

            site, created = SaxonCulturalSite.objects.get_or_create(
                osm_id=props.get('@id'),
                defaults={
                    'name': props.get('name'),
                    'tourism': props.get('tourism'),
                    'website': props.get('website'),
                    'city': props.get('addr:city'),
                    'street': props.get('addr:street'),
                    'postcode': props.get('addr:postcode'),
                    'building': props.get('building'),
                    'wheelchair': props.get('wheelchair'),
                    'wikidata': props.get('wikidata'),
                    'geometry': geometry,
                }
            )
            if created:
                count += 1

        self.stdout.write(self.style.SUCCESS(f'Imported {count} Saxon cultural sites'))
