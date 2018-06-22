from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from userprofile.models import Profile
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 140, default = 'Title')
    body = models.TextField(default = "")
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,default = None,on_delete = models.CASCADE,related_name='%(class)s_author')
    likes = models.ManyToManyField(User,related_name='%(class)s_likes')
    image = models.FileField(null=True, blank=True, upload_to='./ArticleImage/')
    
    def get_absolute_url(self):
        return reverse('articles:detail',kwargs = {'pk':self.pk})
    def __str__(self):
        return self.title
    def snippet(self):
        return self.body[:50]+'[...]'
    def authorcap(self):
        capital = self.author
        capital = str(capital).capitalize()
        return capital
    def authorImg(self):
        profile = Profile.objects.get(author=self.author)
        return profile.user_image.url

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.CharField(max_length = 128)
    pubDateTime = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.article.title + '-' + str(self.id)
    def authorImg(self):
        profile = Profile.objects.get(author=self.user)
        return profile.user_image.url
    class Meta:
        ordering = ['pubDateTime']