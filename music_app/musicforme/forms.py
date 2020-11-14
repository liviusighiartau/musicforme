from django.forms import ModelForm

from musicforme.models import Post


class PostCreationForm(ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'musical_instrument', 'content')

