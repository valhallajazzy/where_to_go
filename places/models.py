from django.conf import settings
from django.db import models
from django.contrib import admin


class Place(models.Model):
    title = models.CharField(max_length=255, blank=False, verbose_name='Заголовок')
    description_short = models.TextField(verbose_name='Короткое описание')
    description_long = models.TextField(verbose_name='Развернутое описание')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')


    def __str__(self):
        return self.title

class Image(models.Model):
    number = models.PositiveIntegerField(verbose_name='Позиция')
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, verbose_name='Картинка')

    def __str__(self):
        return str(self.number) + ' ' + str(self.place)

    @property
    def get_absolute_image_url(self):
        return f'{self.image.url}'

class ImageInline(admin.TabularInline):
    model = Image