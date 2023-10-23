from django.contrib import admin
from .models import Place, ImageInline


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
