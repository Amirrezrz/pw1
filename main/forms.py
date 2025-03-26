from django import forms
from .models import RentAd

class RentAdForm(forms.ModelForm):
    class Meta:
        model = RentAd
        fields = ['title', 'description', 'location', 'price', 'image']
