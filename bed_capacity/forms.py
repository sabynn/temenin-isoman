
from django import forms
from .models import RumahSakit, BedRequest, validate_telp


# creating a form
class BedRequestForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = BedRequest

        # specify fields to be used
        fields = [
            "nama",
            "gender",
            "umur",
            "alamat",
            "telp",
        ]

        widgets = {
            'alamat': forms.Textarea(),
            'gender': forms.RadioSelect(),
            'umur': forms.NumberInput(),
        }

        validators = {
            'telp': [validate_telp]
        }
