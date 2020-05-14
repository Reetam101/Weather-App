from django.forms import ModelForm, TextInput
from .models import City
from django.core.exceptions import ValidationError

class CityForm(ModelForm):

    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'}),
        }