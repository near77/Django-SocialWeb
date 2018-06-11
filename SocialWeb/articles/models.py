from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 140, default = 'Title')
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,default = None,on_delete = models.SET_DEFAULT,related_name='%(class)s_author')
    likes = models.ManyToManyField(User,related_name='%(class)s_likes')
    image = models.FileField(null=True, blank=True, upload_to='./ArticleImage/')
    
    def __str__(self):
        return self.title
    def snippet(self):
        return self.body[:30]+'[...]'
    def authorcap(self):
        capital = self.author
        capital = str(capital).capitalize()
        return capital
