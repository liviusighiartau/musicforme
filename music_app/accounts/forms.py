from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import CustomUser

from django import forms


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'city', 'country', 'address', 'age', 'is_teacher')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class CustomUserForm(forms.Form):
    first_name = forms.CharField(max_length=150, label='First name')
    last_name = forms.CharField(max_length=150, label='Last name')
    username = forms.CharField(max_length=150, label='Username')
    email = forms.EmailField(required=True, label='Email address')
    city = forms.CharField(max_length=60, label='City')
    country = forms.CharField(max_length=56, label='Country')
    address = forms.CharField(max_length=50, label='Address', help_text='Without using special characters')
    age = forms.IntegerField(label='Age', help_text='Insert your age.')
