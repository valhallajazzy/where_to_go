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
            request = requests.get(url)
            json_file = request.json()
            images_urls = json_file['imgs']

        except:
            raise CommandError('Json file "%s" does not exist' % url)

        place, created = Place.objects.get_or_create(
            defaults={'title': json_file.get('title')},
            title=json_file.get('title'),
            short_description=json_file.get('description_short'),
            long_description=json_file.get('description_long'),
            latitude=json_file.get('coordinates')['lat'],
            longitude=json_file.get('coordinates')['lng'],
        )

        for url in images_urls:
            request = requests.get(f'{url}')
            image, created = Picture.objects.get_or_create(
                number=images_urls.index(url)+1,
                place=place,
                image=ContentFile(request.content, name="{}{}".format(json_file['title'], images_urls.index(url))+'.jpg')
            )