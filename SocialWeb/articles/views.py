from django.views.generic.edit import UpdateView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm
from django.shortcuts import get_object_or_404
# Create your views here.

def article_list(request):
    articles = Article.objects.all().order_by('-date')
    return render(request,"articles/articlelist.html", {'articles':articles})