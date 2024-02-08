from django import forms
from .models import Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields= '__all__'
        # fields = ['musician', 'album_name', 'release_date', 'rating']