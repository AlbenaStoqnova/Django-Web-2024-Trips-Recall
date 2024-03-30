from django import forms

from trips_recall.photos.models import TripPhoto


class TripPhotoBaseForm(forms.ModelForm):
    class Meta:
        model = TripPhoto
        fields = ('photo', 'description', 'location', 'trips')


class TripPhotoCreateForm(TripPhotoBaseForm):
    pass


class TripPhotoEditForm(TripPhotoBaseForm):
    pass

