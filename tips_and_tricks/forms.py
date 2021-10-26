from tips_and_tricks.models import TipsAndTrick
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'
    


class AddForm(forms.ModelForm):
    class Meta:
        model = TipsAndTrick
        fields = '__all__'
        widgets = {
            'published_date': DateInput(),
        }