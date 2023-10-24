from django.contrib import admin
from .models import Place, ImageInline, Image
from adminsortable2.admin import SortableAdminBase

@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


