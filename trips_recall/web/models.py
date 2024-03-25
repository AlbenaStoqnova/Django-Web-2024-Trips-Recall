from django.contrib.auth import get_user_model
from django.db import models

from trips_recall.photos.models import TripPhoto


UserModel = get_user_model()


class PhotoComment(models.Model):
    MAX_LENGTH_TEXT = 300
    text = models.TextField(
        max_length=MAX_LENGTH_TEXT,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    modified_at = models.DateTimeField(
        auto_now=True,
    )
    pet_photo = models.ForeignKey(TripPhoto, on_delete=models.RESTRICT,)

    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT,)


class PhotoLike(models.Model):
    pet_photo = models.ForeignKey(TripPhoto, on_delete=models.RESTRICT,)

    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT, )