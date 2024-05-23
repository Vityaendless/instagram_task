from django.urls import path
from django.views.generic.base import RedirectView


app_name = 'webapp'

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='accounts:login'), name='index'),
]