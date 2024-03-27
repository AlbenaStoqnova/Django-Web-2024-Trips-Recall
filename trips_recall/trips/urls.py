from django.urls import path
from trips_recall.trips.views import TripCreateView

urlpatterns = (
    path('create/', TripCreateView.as_view(), name='create trip'),
)
