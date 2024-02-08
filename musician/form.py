from django import forms
from .models import Musician 

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        # fields = '__all__'
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'instrument_type']

 
