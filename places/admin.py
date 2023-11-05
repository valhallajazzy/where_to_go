from django.contrib import admin
from .models import Place, Picture

from adminsortable2.admin import SortableAdminBase, SortableStackedInline


class ImageInline(SortableStackedInline):
    model = Picture
    fields = ('image', 'get_preview_image', 'number')
    readonly_fields = ["get_preview_image"]


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    fields = ['get_preview_image','image', 'number', 'place']
    raw_id_fields = ['place']
    readonly_fields = ["get_preview_image"]