from django.contrib.auth import get_user_model
from django.db import models

from trips_recall.trips.models import Trip


UserModel = get_user_model()


class TripPhoto(models.Model):
    MAX_LENGTH_DESCRIPTION = 300
    MAX_LENGTH_LOCATION = 100

    photo = models.ImageField(
        upload_to='photos/',
        null=False,
        blank=False,
    )
    description = models.CharField(
        max_length=MAX_LENGTH_DESCRIPTION,
        null=True,
        blank=True,

    )
    location = models.CharField(
        max_length=MAX_LENGTH_LOCATION,
        null=True,
        blank=True,
    )
    trips = models.ManyToManyField(Trip)

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    modified_at = models.DateTimeField(
        auto_now=True,
    )
    user = models.ForeignKey(UserModel,
                             on_delete=models.RESTRICT)