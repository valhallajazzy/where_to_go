from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import get_GeoJSON


urlpatterns = [
    path('', get_GeoJSON, name='start_page')
]