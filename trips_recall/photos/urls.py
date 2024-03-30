from django.urls import path
from trips_recall.photos.views import TripPhotoCreateView

urlpatterns = (
    path('create/', TripPhotoCreateView.as_view(), name='create photo'),
)