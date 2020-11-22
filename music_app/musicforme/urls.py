from django.urls import path

from musicforme import views

urlpatterns = [
    path('posts/create/', views.create_post, name='create-post'),
    path('posts/<int:user_id>/', views.user_post_view, name='user-posts'),
    path('posts/<int:user_id>/<int:post_id>/', views.edit_post_view, name='edit-post'),
    path('posts/', views.display_posts, name='display-posts'),
]
