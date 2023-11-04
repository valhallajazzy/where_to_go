from django.db import models
from django.utils.safestring import mark_safe

from adminsortable2.admin import SortableStackedInline
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=255, blank=False, verbose_name='Заголовок', unique=True)
    short_description = models.TextField(blank=True, verbose_name='Короткое описание')
    long_description = HTMLField(blank=True, verbose_name='Развернутое описание')
    latitude = models.FloatField(verbose_name='Широта', unique=True)
    longitude = models.FloatField(verbose_name='Долгота', unique=True)

    def __str__(self):
        return self.title


class Pictures(models.Model):
    number = models.PositiveIntegerField(null=True, blank=True, verbose_name='Позиция', default=0)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Принадлежность локации')
    image = models.ImageField(null=True, blank=True, verbose_name='Картинка', unique=True)

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
    model = Pictures
    fields = ('image', 'place_image', 'number')
    readonly_fields = ["place_image"]