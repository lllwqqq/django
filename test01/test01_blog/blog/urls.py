from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:pk>/', views.detail, name='detail'),
    path('archives/<int:year>/<int:month>/', views.archives, name='archives'),
    path('categories/<int:pk>/', views.category, name='category'),
    path('tags/<int:pk>/', views.tags, name='tags')
]
