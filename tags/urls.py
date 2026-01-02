from django.urls import path
from . import views

urlpatterns = [
    path('tags/create', views.create_tag, name='create_tag'),
    path('tags/', views.tags_list, name='tags_list'),
]
