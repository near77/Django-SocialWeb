from django.views.generic.edit import UpdateView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm
from userprofile.models import Profile
from django.shortcuts import get_object_or_404
# Create your views here.

# def article_list(request):
#     articles = Article.objects.all().order_by('-date')
#     return render(request, "articles/articlelist.html", {'articles':articles})

def article_list(request):
    articles = Article.objects.all().order_by('-date')
    try:
        profile = Profile.objects.get(author = request.user)
    except:
        profile = None
    items = [profile]
    items.extend(list(articles))
    return render(request, 'articles/articlelist.html', {'items':items})

def article_detail(request, pk):
    article = Article.objects.get(pk = pk)
    items = [article]
    items.extend(list(Comment.objects.filter(article = article)))
    return render(request, "articles/article.html", {'items':items})

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

def CommentCreate(request, articleID):
    comment = request.POST.get('comment')
    if comment:
        comment = comment.strip()
    if not comment:
        return redirect('../')
    article = get_object_or_404(Article, id = articleID)
    Comment.objects.create(article = article, user=request.user, content =comment)
    return redirect('../')

def CommentDelete(request, pk):
    if pk!=None:
        if request.method == "POST":
            pk = request.POST['article_id']
        try:
            comment = Comment.objects.get(pk = pk)
            postId = comment.article_id
            comment.delete()
            return redirect('http://127.0.0.1:8000/articles/'+str(postId)+'/')
        except:
            message = "Reading Error"
    return render(request, 'blog/blog.html')