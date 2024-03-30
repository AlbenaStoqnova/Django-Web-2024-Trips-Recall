from django.shortcuts import render, redirect
from trips_recall.trips.models import Trip
from trips_recall.web.forms import CreateProfileForm


def create_profile(request):
    form = CreateProfileForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("index")

    context = {
        "form": form,
        "no_nav": True,
    }

    return render(request, "web/home_page_with_user.html", context)


def index(request):
    context = {
        'trips': Trip.objects.all(),
    }
    return render(request, 'web/index.html', context)

