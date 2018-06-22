from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Profile(models.Model):
    author = models.ForeignKey(User, default = None, on_delete = models.CASCADE,related_name='%(class)s_author')
    user_image = models.FileField(null = True, blank = True, upload_to='./ProfileImage/')
    about_user = models.TextField(default = " ")
    city = models.CharField(default = '',max_length = 50)
    birthday = models.CharField(default = '',max_length = 50)
    follower = models.ManyToManyField(User, blank = True,related_name='%(class)s_follower')
    follow = models.ManyToManyField(User, blank = True,related_name='%(class)s_follow')
    
    def get_absolute_url(self):
        return reverse('userprofile:personal_page',kwargs = {'pk':self.author.id})
    def __str__(self):
        return str(self.author)

class Album(models.Model):
    author = models.ForeignKey(User, default = None, on_delete = models.CASCADE,related_name='%(class)s_author')
    album_image = models.FileField(null = True, blank = True,default = './AlbumImage/album.jpg', upload_to='./AlbumImage/')
    title = models.CharField(max_length = 140, default = 'Album')
    def __str__(self):
        return str(self.title)

class Photo(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE,related_name='%(class)s_author')
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    image = models.FileField( upload_to='./AlbumImage/PhotoImage/')
    def __str__(self):
        return str(self.author)
