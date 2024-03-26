from django.urls import path

from trips_recall.web.views import index

urlpatterns = (
    path('', index, name='index'),
)