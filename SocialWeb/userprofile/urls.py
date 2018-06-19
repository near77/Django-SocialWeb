from django.urls import path
from . import views
app_name = 'userprofile'

urlpatterns = [ path('<int:pk>/', views.personal_page, name = 'personal_page'),
                path('<int:pk>/profileCreate/', views.ProfileCreate, name='profileCreate'),
                path('<int:pk>/update/', views.ProfileUpdate.as_view(), name = 'update'),
                ]