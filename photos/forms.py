from django import forms
from photos.models import Photo

class AddPhoto(forms.ModelForm):
    """Form for users to add new photo"""
    title = forms.CharField(max_length=64, label='Title')
    img = forms.ImageField(label='Photo')
    
    class Meta:
        model = Photo
        fields = ('img', 'title')