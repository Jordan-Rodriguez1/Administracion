from django.forms import ModelForm
from .models import address

class Add_Address(ModelForm):
    class Meta:
        model = address
        fields = ['unit_number', 'street_numbre', 'adrees', 'city', 'postal_code', 'country']