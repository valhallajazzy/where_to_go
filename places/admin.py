from django.contrib import admin
from .models import Place, ImageInline, Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


