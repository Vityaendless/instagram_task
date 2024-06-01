from django.views.generic import View
from django.shortcuts import redirect, get_object_or_404, render

from ..models import Publication, Like


class LikeCreateView(View):
    def get(self, request, *args, **kwargs):
        user = self.request.user
        publication = get_object_or_404(Publication, pk=kwargs.get('pk'))
        like = Like.objects.filter(user=user, publication=publication)
        is_like = False
        if not like:
            Like.objects.create(user=user, publication=publication)
            publication.increase_count('likes')
            is_like = True
        return render(request, 'publications/details.html', {'publication': publication, 'like': is_like})
