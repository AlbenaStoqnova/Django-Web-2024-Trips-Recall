from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinLengthValidator


UserModel = get_user_model()


class Trip(models.Model):

    MAX_LENGTH_TITLE = 50
    MIN_LENGTH_TITLE = 2
    MAX_LENGTH_LOCATION = 100
    MAX_LENGTH_DESCRIPTION = 300

    title = models.CharField(
        max_length=MAX_LENGTH_TITLE,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(MIN_LENGTH_TITLE),
        ),
    )
    trip_photo = models.ImageField(
        upload_to='trip_photos/',
        default='trip_photos/default_photo.jpg',
        null=False,
        blank=False
    )
    location = models.CharField(
        max_length=MAX_LENGTH_LOCATION,
        null=True,
        blank=True,
    )
    date_created = models.DateTimeField(
        auto_now_add=True
    )
    date_of_trip = models.DateField()
    description = models.CharField(
        max_length=MAX_LENGTH_DESCRIPTION,
        null=True,
        blank=True,
    )
    user = models.ForeignKey(UserModel,
                             on_delete=models.RESTRICT)