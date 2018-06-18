from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    author = models.ForeignKey(User, default = None, on_delete = models.CASCADE)
    user_image = models.FileField(null = True, blank = True, upload_to='./ProfileImage/')
    about_user = models.TextField(default = " ")

    def __str__(self):
        return str(self.author)