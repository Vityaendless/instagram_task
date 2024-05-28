from django.views.generic import CreateView
from django.shortcuts import redirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from ..models import Publication
from ..forms import PublicationForm, SearchForm


class PublicationCreateView(CreateView):
    template_name = 'publications/new.html'
    model = Publication
    form_class = PublicationForm
    # permission_required = 'webapp.add_project'

    def form_valid(self, form):
        publication = form.save(commit=False)
        publication.author = self.request.user
        publication.save()
        # return redirect('webapp:publication', pk=publication.pk)
        return redirect('accounts:login')

    #наложить пермишены
    #правильная переадресация
    #менять счетчик публикаций

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['search_form'] = SearchForm(self.request.GET)
        return context
