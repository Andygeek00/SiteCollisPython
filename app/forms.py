from django import forms
from .models import Parcel

class RegisterParcelForm(forms.ModelForm):
    class Meta:
        model = Parcel
        fields = ['Adress_dep','Arr_dep','Weight']
        