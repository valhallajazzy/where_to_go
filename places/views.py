import json
from pprint import pprint

from django.core import serializers
from django.http import JsonResponse, HttpResponse

from .models import Place, Image
from django.shortcuts import render, get_object_or_404


# Create your views here.
def get_GeoJSON(request):
    moscow_legends_coordinates = Place.objects.get(title='Экскурсионный проект «Крыши24.рф»').coordinates
    roofs24_coordinates = Place.objects.get(title='Экскурсионная компания «Легенды Москвы»').coordinates
    geo_json = \
    {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [f'{float(moscow_legends_coordinates["lng"])}', f'{float(moscow_legends_coordinates["lat"])}']
                },
                "properties": {
                    "title": "«Легенды Москвы",
                    "placeId": "moscow_legends",
                    "detailsUrl": "static/places/moscow_legends.json"
                }
            },
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [f'{float(roofs24_coordinates["lng"])}', f'{float(roofs24_coordinates["lat"])}']
                },
                "properties": {
                    "title": "Крыши24.рф",
                    "placeId": "roofs24",
                    "detailsUrl": "static/places/roofs24.json"
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
        "coordinates": location.coordinates
    }
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False, 'indent': 4})
