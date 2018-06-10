from django.urls import path, include
from . import views
urlpatterns = [
    path('signup/', views.signup, name = 'signup'),
    path('', views.login, name = 'login'),
    path('', views.logout, name = 'logout')
]