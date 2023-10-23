import json
from pprint import pprint

from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.urls import reverse

from .models import Place, Image
from django.shortcuts import render, get_object_or_404


def get_GeoJSON(request):
    moscow_legends_coordinates = [float(Place.objects.get(id=1).longitude), float(Place.objects.get(id=1).latitude)]
    roofs24_coordinates = [float(Place.objects.get(id=2).longitude), float(Place.objects.get(id=2).latitude)]
    geo_json = \
    {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": moscow_legends_coordinates
                },
                "properties": {
                    "title": "«Легенды Москвы",
                    "placeId": "moscow_legends",
                    "detailsUrl": reverse('JSONdata', kwargs={'id': 1})
                }
            },
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": roofs24_coordinates

                },
                "properties": {
                    "title": "Крыши24.рф",
                    "placeId": "roofs24",
                    "detailsUrl": reverse('JSONdata', kwargs={'id': 2})
                }
            }
        ]
    }
    return render(request, "index.html", {"geo_json": geo_json})


def get_JSONdata(request, id):
    location = get_object_or_404(Place, id=id)
    image = Image.objects.filter(place=id)
    image_url_list = []
    for elem in image:
        image_url_list.append(elem.get_absolute_image_url)
    data = {
        "title": location.title,
        "imgs": image_url_list,
        "description_short": location.description_short,
        "description_long": location.description_long,
        "coordinates": {'lat': location.latitude, 'lng': location.longitude }
    }
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False, 'indent': 4})
