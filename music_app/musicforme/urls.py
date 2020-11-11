from django.urls import path

from musicforme.views import CreateInstrumentView

urlpatterns = [
    path('signup/', CreateInstrumentView, name='signup'),
]