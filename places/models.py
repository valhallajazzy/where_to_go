from django.conf import settings
from django.contrib.admin.options import InlineModelAdmin
from django.db import models
from django.contrib import admin
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableStackedInline
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=255, blank=False, verbose_name='Заголовок')
    description_short = models.TextField(verbose_name='Короткое описание')
    description_long = HTMLField(verbose_name='Развернутое описание')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')



    def __str__(self):
        return self.title

class Image(models.Model):
    number = models.PositiveIntegerField(verbose_name='Позиция', default=0)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, verbose_name='Картинка')

    def __str__(self):
        return str(self.number) + ' ' + str(self.place)

    @property
    def get_absolute_image_url(self):
        return f'{self.image.url}'

    def place_image(self):
        return mark_safe('<img src="{}" height="150" />'.format(self.image.url))

    class Meta:
        ordering = ['number']




class ImageInline(SortableStackedInline):
    model = Image
    fields = ('image', 'place_image', 'number')
    readonly_fields = ["place_image"]