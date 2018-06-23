from django.shortcuts import render
from articles.models import Article
from .models import Profile, Album, Photo
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, AlbumForm, PhotoForm
# Create your views here.

def personal_page(request, pk):
    try:
        profile = Profile.objects.get(author_id = pk)
    except:
        profile = None
    items = [profile]
    items.extend(list(Article.objects.filter(author_id = pk).order_by('-date')))
    followers = []
    follows = []
    for item in profile.follower.all():
        followers.append(Profile.objects.get(author = item))
    for item in profile.follow.all():
        follows.append(Profile.objects.get(author = item))
    if items:
        return render(request, 'userprofile/personalpage.html',{'items':items,'followers':followers,'follows':follows})
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

def Follow(request, pk):
    try:
        profile = Profile.objects.get(author_id = pk)
    except:
        profile = None
    items = [profile]
    items.extend(list(Article.objects.filter(author_id = pk).order_by('-date')))
    next = request.GET.get('next', '/')
    profile2 = Profile.objects.get(author_id = request.user.id)
    if request.user not in profile.follower.all():
        profile.follower.add(request.user)
        profile2.follow.add(profile.author)
        return redirect('../')
    else:
        profile.follower.remove(request.user)
        profile2.follow.remove(profile.author)
        return redirect('../')
    return render(request, 'userprofile/personalpage.html',{'items':items})

def album(request, pk):
    profile = Profile.objects.get(author_id = pk)
    items = [profile]
    try:
        albums = Album.objects.filter(author_id = pk)
    except:
        albums = None
    return render(request, 'userprofile/album.html',{'items':items,'albums':albums})

@login_required(login_url = '/login/')
def AlbumCreate(request, pk):
    if request.method == 'POST':
        form = AlbumForm(request.POST , request.FILES)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect('../')
    else:
        form = AlbumForm()
        return render(request, 'userprofile/album_form.html', {'form':form})

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['album_image','title']

def AlbumDelete(request, pk):
    if pk != None:
        if request.method == "POST":
            pk = request.POST['item_id']
        try:
            album = Album.objects.get(pk=pk)
            album.delete()
            return redirect('/userprofile/'+str(album.author_id)+'/album/')
        except:
            message = "Error"
    return render(request,"articles/articlelist.html")

def photo(request, pk):
    album = Album.objects.get(id = pk)
    user_id = album.author_id
    profile = Profile.objects.get(author_id = user_id)
    try:
        photo = Photo.objects.filter(album_id = pk)
    except:
        photo = None
    return render(request, 'userprofile/photo.html',{'photo':photo,'item':profile,'album':album})

def PhotoCreate(request, pk):
    if request.method == 'POST':
        form = PhotoForm(request.POST , request.FILES)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.author = request.user
            instance.album = Album.objects.get(id = pk)
            instance.save()
            return redirect('../')
    else:
        form = PhotoForm()
        return render(request, 'userprofile/photo_form.html', {'form':form})

class PhotoUpdate(UpdateView):
    model = Photo
    fields = ['image']

def PhotoDelete(request, pk):
    if pk != None:
        if request.method == "POST":
            pk = request.POST['item_id']
        try:
            photo = Photo.objects.get(pk=pk)
            photo.delete()
            return redirect('/userprofile/album/'+str(photo.album_id)+'/')
        except:
            message = "Error"
    return render(request,"articles/articlelist.html")
