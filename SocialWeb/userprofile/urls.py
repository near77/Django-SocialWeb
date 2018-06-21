from django.urls import path
from . import views
app_name = 'userprofile'

urlpatterns = [ path('<int:pk>/', views.personal_page, name = 'personal_page'),
                path('profile/add/', views.ProfileCreate, name='profileCreate'),
                path('<int:pk>/update/', views.ProfileUpdate.as_view(), name = 'update'),
                path('<int:pk>/follow/', views.Follow, name = 'follow'),
                ]