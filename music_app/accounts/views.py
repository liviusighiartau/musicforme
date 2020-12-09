from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from accounts.forms import CustomUserCreationForm, CustomUserForm
from accounts.models import CustomUser


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def edit_account_view(request, **kwargs):
    account_id = kwargs['account_id']
    user = get_object_or_404(CustomUser, id=account_id)
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            CustomUser.objects.filter(id=account_id).update(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                country=form.cleaned_data['country'],
                age=form.cleaned_data['age'],
                city=form.cleaned_data['city'],
                address=form.cleaned_data['address']
            )
            return HttpResponseRedirect(reverse('home'))
    else:
        form = CustomUserForm(
            {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'username': user.username,
                'email': user.email,
                'country': user.country,
                'city': user.city,
                'address': user.address,
                'age': user.age
            }
        )

    return render(request, 'accounts/account_details.html', {'form': form})
