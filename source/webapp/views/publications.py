from django.views.generic import CreateView, DetailView
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from ..models import Publication
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

    #правильная переадресация

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
