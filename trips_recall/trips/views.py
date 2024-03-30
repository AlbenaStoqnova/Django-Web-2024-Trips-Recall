from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic as views
from trips_recall.trips.forms import TripCreateForm, TripEditForm, TripDeleteForm
from trips_recall.trips.models import Trip


class TripCreateView(views.CreateView):
    form_class = TripCreateForm
    template_name = 'trips/create_trip.html'

    def get_success_url(self):
        return reverse('my trips', kwargs={
            'email': self.object.email,
        })

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.instance.user = self.request.user
        return form


class TripEditView(views.UpdateView):
    model = Trip
    form_class = TripEditForm
    template_name = 'trips/edit_trip.html'
    success_url = reverse_lazy('my trips')


class TripDeleteView(views.DeleteView):
    model = Trip
    form_class = TripDeleteForm

    template_name = "trips/delete_trip.html"

    success_url = reverse_lazy('my trips')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object
        return kwargs