from django.urls import path
from . import views
app_name = 'userprofile'

urlpatterns = [ path('<int:pk>/', views.personal_page, name = 'personal_page'),
                path('profile/add/', views.ProfileCreate, name='profileCreate'),
                path('<int:pk>/update/', views.ProfileUpdate.as_view(), name = 'update'),
                path('<int:pk>/follow/', views.Follow, name = 'follow'),
                path('<int:pk>/album/', views.album, name = 'album'),
                path('<int:pk>/album/add/', views.AlbumCreate, name = 'albumCreate'),
                path('<int:pk>/album/update/', views.AlbumUpdate.as_view(), name = 'albumupdate'),
                path('<int:pk>/album/delete/', views.AlbumDelete, name = 'albumdelete'),
                path('album/<int:pk>/', views.photo, name = 'photo'),
                path('album/<int:pk>/add/', views.PhotoCreate, name = 'photoCreate'),
                path('album/<int:pk>/delete/', views.PhotoDelete, name = 'photodelete'),
                ]