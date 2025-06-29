import csv
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point
from pyproj import Transformer
from core.models import MotorhomeParking

class Command(BaseCommand):
    help = 'Import Motorhome Parking data from CSV and convert coordinates to EPSG:4326'

    def handle(self, *args, **kwargs):
        transformer = Transformer.from_crs(3857, 4326, always_xy=True)

        with open('D:\\Python\\Cultural-Mapping\\server\\core\\data\\Parkplätze_Wohnmobil.csv', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            for row in reader:
                x = float(row.get('X'))
                y = float(row.get('Y'))
                lon, lat = transformer.transform(x, y)  # Convert to lat/lon

                MotorhomeParking.objects.create(
                    number=row.get('NUMMER'),
                    location=row.get('LAGE'),
                    capacity=row.get('KAPAZITAET'),
                    cost=row.get('KOSTEN'),
                    remarks=row.get('BEMERKUNG', ''),
                    x=x,
                    y=y,
                    point=Point(lon, lat, srid=4326)
                )

        self.stdout.write(self.style.SUCCESS('Motorhome parking data imported successfully.'))
