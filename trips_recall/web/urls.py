from django.urls import path

from trips_recall.web.views import index, my_trips

urlpatterns = (
    path('', index, name='index'),
    path('my/trips/', my_trips, name='my trips'),
)