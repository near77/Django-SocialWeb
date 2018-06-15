from django.views.generic.edit import UpdateView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm
from django.shortcuts import get_object_or_404
# Create your views here.

def article_list(request):
    articles = Article.objects.all().order_by('-date')
    return render(request, "articles/articlelist.html", {'articles':articles})

def article_detail(request, pk):
    article = Article.objects.get(pk = pk)
    return render(request, "articles/article.html", {'article':article})

@login_required(login_url = '/login/')
def ArticleCreate(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST or None , request.FILES or None)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = ArticleForm()
        return render(request, 'articles/article_form.html', {'form':form})

def ArticleDelete(request, pk):
    if pk != None:
        if request.method == "POST":
            pk = request.POST['article_id']
        try:
            article = Article.objects.get(pk=pk)
            article.delete()
            return redirect('articles:list')
        except:
            message = "Error"
    return render(request,"articles/articlelist.html")

def ArticleLike(request, pk):
    article = Article.objects.get(pk = pk)
    next = request.GET.get('next', '/')
    if request.user not in article.likes.all():
        article.likes.add(request.user)
        return redirect('../')
    else:
        article.likes.remove(request.user)
        return redirect('../')
    return render(request, "articles/article.html", {'article':article})

class ArticleUpdate(UpdateView):
    model = Article
    fields = ['title','body','image']
    