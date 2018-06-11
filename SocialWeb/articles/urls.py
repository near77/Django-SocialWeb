from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [ path('', views.article_list, name = 'list'),
                path('<int:pk>/', views.article_detail, name = 'detail'),
                path('article/add/', views.ArticleCreate, name = 'create')]
