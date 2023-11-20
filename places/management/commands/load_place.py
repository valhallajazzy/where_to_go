from django.core.management.base import BaseCommand, CommandError
import requests
from places.models import *
from django.core.files.base import ContentFile


class Command(BaseCommand):
    help = 'Create objects in DataBase from provide JSON in URL adress'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str)

    def handle(self, *args, **options):
        try:
            url = options['url']
            response = requests.get(url)
            location = response.json()
            images_urls = location['imgs']

        except:
            raise CommandError('Json file "%s" does not exist' % url)

        place, created = Place.objects.get_or_create(
            title=location.get('title'),
            defaults={
                'short_description': location.get('description_short'),
                'long_description': location.get('description_long'),
                'latitude': location.get('coordinates')['lat'],
                'longitude': location.get('coordinates')['lng'],
            }
        )

        for number, url in enumerate(images_urls):
            response = requests.get(url)
            image, created = Picture.objects.get_or_create(
                number=number,
                place=place,
                image=ContentFile(response.content, name="{}{}".format(location['title'], number)+'.jpg')
            )