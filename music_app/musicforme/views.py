from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from musicforme.forms import PostCreationForm
from musicforme.models import Post


def display_posts(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


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
