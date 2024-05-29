from django.urls import path
from django.views.generic.base import RedirectView
from .views import permission_denied, PublicationCreateView


app_name = 'webapp'

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='accounts:login'), name='index'),
    path('403/', permission_denied, name='403'),
    path('profile/<int:pk>/new_publication/', PublicationCreateView.as_view(), name='new_publication'),
]
