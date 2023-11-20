from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import render, get_object_or_404

from .models import Place, Picture


def put_map_locations(request):
    location = {
        "type": "FeatureCollection",
        "features": []
    }

    places = Place.objects.all()
    for place in places:
        coordinates = [place.longitude, place.latitude]
        location['features'].append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": coordinates
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": reverse('json_data', kwargs={'id': place.id})
                }
            }
        )

    return render(request, "index.html", {"geo_json": location})


def get_json_data(request, id):
    location = get_object_or_404(Place.objects.prefetch_related('pictures'), id=id)
    images = location.pictures.all()
    images_urls = [image.get_absolute_image_url for image in images]
    place_serialize = {
        "title": location.title,
        "imgs": images_urls,
        "description_short": location.short_description,
        "description_long": location.long_description,
        "coordinates": {'lat': location.latitude, 'lng': location.longitude}
    }
    return JsonResponse(place_serialize, json_dumps_params={'ensure_ascii': False, 'indent': 4})
