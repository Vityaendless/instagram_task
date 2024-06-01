from django.urls import path
from django.views.generic.base import RedirectView

from .views import (permission_denied, PublicationCreateView, PublicationView, SubscriptionCreateView,
                    SubscribersListView, SubscribitionsListView, LikeCreateView, CommentCreateView)


app_name = 'webapp'

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='accounts:login'), name='index'),
    path('403/', permission_denied, name='403'),
    path('profile/<int:pk>/new_publication/', PublicationCreateView.as_view(), name='new_publication'),
    path('profile/<int:pk>/details', PublicationView.as_view(), name='publication_details'),
    path('subscription/<int:pk>/', SubscriptionCreateView.as_view(), name='subscription'),
    path('subscribers/<int:pk>/', SubscribersListView.as_view(), name='subscribers'),
    path('subscribitions/<int:pk>/', SubscribitionsListView.as_view(), name='subscribitions'),
    path('like/<int:pk>/', LikeCreateView.as_view(), name='like'),
    path('comment/<int:pk>/', CommentCreateView.as_view(), name='new_comment'),
]
