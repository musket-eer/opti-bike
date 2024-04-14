# your_app_name/forms.py

from django import forms

class BicycleRequestForm(forms.Form):
    email = forms.EmailField(label='Email', required=True)
    location = forms.CharField(label='Location', max_length=100, required=True)
    time_from = forms.TimeField(label='Time From', required=True, widget=forms.TimeInput(attrs={'type': 'time'}))
    time_to = forms.TimeField(label='Time To', required=True, widget=forms.TimeInput(attrs={'type': 'time'}))
