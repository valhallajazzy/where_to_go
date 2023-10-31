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
            r = requests.get(url)
            json_file = r.json()
            images_url_list = json_file['imgs']

        except:
            raise CommandError('Json file "%s" does not exist' % url)

        pls, created = Place.objects.get_or_create(
            title=json_file.get('title'),
            description_short=json_file.get('description_short'),
            description_long=json_file.get('description_long'),
            latitude=json_file.get('coordinates')['lat'],
            longitude=json_file.get('coordinates')['lng'],
        )

        for url in images_url_list:
            r = requests.get(f'{url}')
            photo = ContentFile(r.content)
            img, created = Pictures.objects.get_or_create(
                number=images_url_list.index(url)+1,
                place=pls
            )
            img.image.save("{}{}".format(json_file['title'], images_url_list.index(url))+'.jpg', photo, save=True),
