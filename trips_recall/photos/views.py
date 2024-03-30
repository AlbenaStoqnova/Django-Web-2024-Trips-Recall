
from django.urls import reverse, reverse_lazy
from django.views import generic as views
from trips_recall.photos.forms import TripPhotoCreateForm, TripPhotoEditForm
from trips_recall.photos.models import TripPhoto


class TripPhotoCreateView(views.CreateView):
    form_class = TripPhotoCreateForm
    template_name = 'photos/create_photo.html'
    queryset = TripPhoto.objects.all() \
        .prefetch_related('trips')
    success_url = reverse_lazy('my trips')

    # def get_success_url(self):
    #     return reverse('index', kwargs={
    #         'pk': self.object.pk,
    #     })

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.instance.user = self.request.user
        return form


class TripPhotoDetailView(views.DetailView):
    queryset = TripPhoto.objects.all() \
        .prefetch_related("photolike_set") \
        .prefetch_related("photocomment_set") \
        .prefetch_related("trips")

    template_name = "photos/details_photo.html"