from django.conf import settings
from django.db import models




class Place(models.Model):
    title = models.CharField(max_length=255, blank=False)
    description_short = models.TextField()
    description_long = models.TextField()
    coordinates = models.JSONField()

    def __str__(self):
        return self.title

class Image(models.Model):
    number = models.PositiveIntegerField()
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.number) + ' ' + str(self.place)

    @property
    def get_absolute_image_url(self):
        return f'{self.image.url}'
