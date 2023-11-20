from django.urls import path, include

from .views import put_map_locations, get_json_data


urlpatterns = [
    path('', put_map_locations, name='start_page'),
    path('places/<int:id>', get_json_data, name='json_data'),
    path('tinymce/', include('tinymce.urls')),
]





