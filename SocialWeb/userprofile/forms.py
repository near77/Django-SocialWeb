from django import forms
from .models import Profile, Album

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'user_image', 'about_user', 'city', 'birthday']

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [ 'album_image', 'title']