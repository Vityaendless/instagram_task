from django.views.generic import CreateView, DetailView
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import UserPassesTestMixin

from ..models import Publication, Like, Comment
from ..forms import PublicationForm, SearchForm


class PublicationCreateView(UserPassesTestMixin, CreateView):
    template_name = 'publications/new.html'
    model = Publication
    form_class = PublicationForm

    def form_valid(self, form):
        publication = form.save(commit=False)
        publication.author = self.request.user
        publication.save()
        publication.author.increase_count('publications')
        # return redirect('webapp:publication', pk=publication.pk)
        return redirect('accounts:login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['search_form'] = SearchForm(self.request.GET)
        return context

    def test_func(self):
        return self.request.user.pk == self.kwargs.get('pk')

    def handle_no_permission(self):
        return redirect('webapp:403')


class PublicationView(DetailView):
    model = Publication
    template_name = 'publications/details.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['search_form'] = SearchForm(self.request.GET)
        publication = get_object_or_404(Publication, pk=self.kwargs.get('pk'))
        like = Like.objects.filter(user=self.request.user, publication=publication)
        if not like:
            context['like'] = False
        else:
            context['like'] = True
        comments = Comment.objects.filter(publication=publication)
        context['comments'] = comments
        return context
