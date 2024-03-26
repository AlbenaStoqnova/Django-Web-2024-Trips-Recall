from django import forms
from trips_recall.trips.models import Trip


class ReadonlyFieldsFormMixin:
    readonly_fields = ()

    def _apply_readonly_on_fields(self):
        for field_name in self.readonly_field_names:
            self.fields[field_name].widget.attrs['readonly'] = 'readonly'

    @property
    def readonly_field_names(self):
        if self.readonly_fields == "__all__":
            return self.fields.keys()

        return self.readonly_fields


class TripBaseForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ('title', 'trip_photo', 'location', 'date_of_trip', 'description')

        widgets = {
            'title': forms.TimeInput(attrs={'placeholder': 'Trip title'}),
            'location': forms.TextInput(attrs={'placeholder': 'Location'}),
            'date_of_trip': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.TextInput(attrs={'placeholder': 'Description'})
        }
        labels = {
            'title': 'Trip title:',
            'trip_photo': 'Attach a photo:',
        }


class TripCreateForm(TripBaseForm):
    pass


class TripEditForm(TripBaseForm):
    pass


class TripDeleteForm(ReadonlyFieldsFormMixin, TripBaseForm):
    readonly_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_readonly_on_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance