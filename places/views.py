from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import render, get_object_or_404

from .models import Place, Pictures


def get_geo_json(request):
    geo_json = \
    {
        "type": "FeatureCollection",
        "features": []
    }

    places = Place.objects.all()
    for place in places:
        coordinates = [place.longitude, place.latitude]
        geo_json['features'].append(
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

    return render(request, "index.html", {"geo_json": geo_json})


def get_json_data(request, id):
    location = get_object_or_404(Place, id=id)
    image = Pictures.objects.filter(place=id)
    image_url_list = []
    for elem in image:
        image_url_list.append(elem.get_absolute_image_url)
    data = {
        "title": location.title,
        "imgs": image_url_list,
        "description_short": location.short_description,
        "description_long": location.long_description,
        "coordinates": {'lat': location.latitude, 'lng': location.longitude}
    }
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False, 'indent': 4})
