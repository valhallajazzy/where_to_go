from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import get_geo_json, get_json_data


urlpatterns = [
    path('', get_geo_json, name='start_page'),
    path('places/<int:id>', get_json_data, name='json_data'),
    path('tinymce/', include('tinymce.urls')),
]





