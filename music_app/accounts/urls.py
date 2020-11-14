from django.urls import path

from accounts.views import SignUpView, edit_account_view

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('<int:account_id>/', edit_account_view, name='edit-account'),
]
