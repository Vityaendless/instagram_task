from django.views.generic import View
from django.shortcuts import redirect, get_object_or_404

from ..models import Publication, Like


class LikeCreateView(View):
    def get(self, request, *args, **kwargs):
        user = self.request.user
        publication = get_object_or_404(Publication, pk=kwargs.get('pk'))
        like = Like.objects.filter(user=user, publication=publication)
        if not like:
            Like.objects.create(user=user, publication=publication)
            publication.increase_count('likes')
        return redirect('webapp:publication_details', pk=publication.pk)
