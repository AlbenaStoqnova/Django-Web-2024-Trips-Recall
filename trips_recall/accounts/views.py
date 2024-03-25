
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views, login, logout
from django.urls import reverse_lazy, reverse
from django.views import generic as views
from trips_recall.accounts.forms import TripsRecallUserCreationForm
from trips_recall.accounts.models import Profile



class SignInUserView(auth_views.LoginView):
    template_name = 'accounts/signin_user.html'
    redirect_authenticated_user = True


class SignUpUserView(views.CreateView):
    template_name = 'accounts/signup_user.html'
    form_class = TripsRecallUserCreationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, form.instance)

        return result


def signout_user(request):
    logout(request)
    return redirect('index')


class ProfileUpdateView(views.UpdateView):
    queryset = Profile.objects.all()
    template_name = 'accounts/edit_profile.html'
    fields = ('first_name', 'last_name', 'date_of_birth', 'profile_picture')

    def get_success_url(self):
        return reverse('details profile', kwargs={
            'pk': self.object.pk,
        })

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.fields['date_of_birth'].widget.attrs['type'] = 'date'
        form.fields['date_of_birth'].label = 'Birthday'
        return form


class ProfileDetailsView(views.DetailView):
    queryset = Profile.objects \
        .prefetch_related('user') \
        .all()

    template_name = 'accounts/details_profile.html'


class ProfileDeleteView(views.DeleteView):
    queryset = Profile.objects.all()
    template_name = 'accounts/delete_profile.html'

