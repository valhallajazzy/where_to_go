from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import render

from .models import Place, Picture


def get_geo_json(request):
    geo_data = {
        "type": "FeatureCollection",
        "features": []
    }

    places = Place.objects.all()
    for place in places:
        coordinates = [place.longitude, place.latitude]
        geo_data['features'].append(
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

    return render(request, "index.html", {"geo_json": geo_data})


def get_json_data(request, id):
    location = Picture.objects.prefetch_related('place').filter(place=id)
    image_urls = [image.get_absolute_image_url for image in location]
    place_serialize = {
        "title": location[0].place.title,
        "imgs": image_urls,
        "description_short": location[0].place.short_description,
        "description_long": location[0].place.long_description,
        "coordinates": {'lat': location[0].place.latitude, 'lng': location[0].place.longitude}
    }
    return JsonResponse(place_serialize, json_dumps_params={'ensure_ascii': False, 'indent': 4})
