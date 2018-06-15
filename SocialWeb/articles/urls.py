from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [ path('', views.article_list, name = 'list'),
                path('<int:pk>/', views.article_detail, name = 'detail'),
                path('article/add/', views.ArticleCreate, name = 'create'),
                path('<int:pk>/delete/', views.ArticleDelete, name = 'delete'),
                path('<int:pk>/like/', views.ArticleLike, name = 'like'),
                path('<int:pk>/update/', views.ArticleUpdate.as_view(), name = 'update')]
