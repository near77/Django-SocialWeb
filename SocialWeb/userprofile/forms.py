from django import forms
from .models import Profile, Album, Photo

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'user_image', 'about_user', 'city', 'birthday']

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [ 'album_image', 'title']

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image']