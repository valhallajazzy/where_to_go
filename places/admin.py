from django.contrib import admin
from .models import Place, ImageInline, Pictures

from adminsortable2.admin import SortableAdminBase


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


