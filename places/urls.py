from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import get_GeoJSON, get_JSONdata


urlpatterns = [
    path('', get_GeoJSON, name='start_page'),
    path('places/<int:id>', get_JSONdata, name='JSONdata')
]