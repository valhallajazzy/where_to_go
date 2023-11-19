from django.db import models
from django.utils.html import format_html

from adminsortable2.admin import SortableStackedInline
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=255, blank=False, verbose_name='Заголовок', unique=True)
    short_description = models.TextField(blank=True, verbose_name='Короткое описание')
    long_description = HTMLField(blank=True, verbose_name='Развернутое описание')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return self.title


class Picture(models.Model):
    number = models.PositiveIntegerField(blank=True, verbose_name='Позиция', default=0)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='pictures', verbose_name='Принадлежность локации')
    image = models.ImageField(verbose_name='Картинка', unique=True)

    class Meta:
        ordering = ['number']

    def __str__(self):
        return f'{self.number} {self.place}'

    @property
    def get_absolute_image_url(self):
        return f'{self.image.url}'

    def get_preview_image(self):
        return format_html('<img src="{}" style="max-height:200px" />', self.image.url)

