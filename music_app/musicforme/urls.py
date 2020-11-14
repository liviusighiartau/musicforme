from django.urls import path

from musicforme import views

urlpatterns = [
    path('posts/create/', views.create_post, name='create-post'),
    path('posts/', views.display_posts, name='display-posts'),
]
