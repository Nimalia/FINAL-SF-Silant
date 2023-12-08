from django import forms
from .models import *


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'


class TechserviceForm(forms.ModelForm):
    class Meta:
        model = Techservice
        fields = '__all__'



class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claim
        fields = '__all__'
