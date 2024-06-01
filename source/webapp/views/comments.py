from django.shortcuts import redirect, get_object_or_404
from django.views.generic import CreateView

from ..models import Comment, Publication
from ..forms import CommentForm


class CommentCreateView(CreateView):
    template_name = 'comments/comment_create.html'
    model = Comment
    form_class = CommentForm

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('webapp:403')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        publication = get_object_or_404(Publication, pk=self.kwargs.get('pk'))
        comment = form.save(commit=False)
        comment.publication = publication
        comment.author = self.request.user
        comment.save()
        publication.increase_count('comments')
        return redirect('webapp:publication_details', pk=publication.pk)
