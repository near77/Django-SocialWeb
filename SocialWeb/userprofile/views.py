from django.shortcuts import render
from articles.models import Article
from .models import Profile
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
# Create your views here.

def personal_page(request, pk):
    try:
        profile = Profile.objects.get(author_id = pk)
    except:
        profile = None
    items = [profile]
    items.extend(list(Article.objects.filter(author_id = pk).order_by('-date')))
    if items:
        return render(request, 'userprofile/personalpage.html',{'items':items})
    else:
        return render(request, 'userprofile/personalpage.html',{'pk':pk})

@login_required(login_url = '/login/')
def ProfileCreate(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST or None , request.FILES or None)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = ProfileForm()
        return render(request, 'userprofile/profile_form.html', {'form':form})


class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['about_user','user_image','city','birthday']