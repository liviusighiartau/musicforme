from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from accounts.models import CustomUser
from musicforme.forms import PostCreationForm
from musicforme.models import Post


def display_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts/display_posts.html', {'posts': posts})


def create_post(request, **kwargs):
    if request.method == 'POST':
        form = PostCreationForm(request.POST)
        if form.is_valid():
            Post.objects.create(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
                musical_instrument=form.cleaned_data['musical_instrument'],
                author=request.user
            )
            return HttpResponseRedirect(reverse('home'))
    else:
        form = PostCreationForm()

    return render(request, 'posts/create_post.html', {'form': form})


def user_post_view(request, **kwargs):
    user_id = kwargs['user_id']
    posts = Post.objects.filter(author_id=user_id)
    return render(request, 'posts/display_posts.html', {'posts': posts})


def edit_post_view(request, **kwargs):
    post_id = kwargs['post_id']
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostCreationForm(request.POST)
        if form.is_valid():
            Post.objects.filter(id=post_id).update(
                title=form.cleaned_data['title'],
                musical_instrument=form.cleaned_data['musical_instrument'],
                content=form.cleaned_data['content']
            )
            return HttpResponseRedirect(reverse('display-posts'))
    else:
        form = PostCreationForm(
            {
                'title': post.title,
                'musical_instrument': post.musical_instrument,
                'content': post.content
            }
        )
    return render(request, 'posts/edit_post.html', {'form': form})
