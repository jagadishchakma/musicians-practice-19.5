from django import forms 
from . import models

class AlbumForm(forms.ModelForm):
    release_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = models.Album
        fields = '__all__'
