from django.urls import path
from trips_recall.trips.views import TripCreateView, TripEditView, TripDeleteView

urlpatterns = (
    path('create/', TripCreateView.as_view(), name='create trip'),
    path('edit/<int:pk>/', TripEditView.as_view(), name='edit trip'),
    path('delete/<int:pk>', TripDeleteView.as_view(), name='delete trip'),
)
