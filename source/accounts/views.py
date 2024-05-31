from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth import login, logout, get_user_model
from django.views.generic import DetailView, CreateView, UpdateView, ListView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Q
from django.utils.http import urlencode

from .auth import EmailUsernameAuthentication as EUA
from .forms import UserForm
from webapp.forms import SearchForm
from webapp.models import Subscription, Publication


User_model = get_user_model()


def login_view(request):
    context = {}
    context['search_form'] = SearchForm(request.GET)
    if request.user.is_authenticated:
        user = get_object_or_404(User_model, pk=request.user.pk)
        subscribe = Subscription.objects.filter(user=user)
        if subscribe:
            subscribitions_pk = []
            for subscribition in subscribe:
                subscribitions_pk.append(subscribition.subscriber.pk)
            context['subscribitions_publications'] = Publication.objects.filter(author__in=subscribitions_pk).order_by('-created_at')
    if request.method == 'POST':
        login_data = request.POST.get('login_data')
        password = request.POST.get('password')
        user = EUA.authenticate(request, login_data, password)
        if user is not None:
            login(request, user)
            return redirect('accounts:login')
        else:
            context['has_error'] = True
    return render(request, 'login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('accounts:login')


class UserView(DetailView):
    model = User_model
    template_name = 'profile.html'
    context_object_name = 'user_obj'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['publications'] = self.object.publications.all()
        context['search_form'] = SearchForm(self.request.GET)
        if self.request.user.pk != self.kwargs.get('pk'):
            user_from_profile = User_model.objects.get(pk=self.kwargs.get('pk'))
            subscribe = Subscription.objects.filter(user=self.request.user, subscriber=user_from_profile)
            if subscribe:
                context['subscribe'] = True
        return context


class RegisterView(CreateView):
    model = get_user_model()
    form_class = UserForm
    template_name = 'registration.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('webapp:403')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_page = reverse('accounts:login')
        return next_page


class UserUpdateView(UserPassesTestMixin, UpdateView):
    template_name = 'edit_profile.html'
    model = User_model
    form_class = UserForm

    def test_func(self):
        return self.request.user.pk == self.kwargs.get('pk')

    def handle_no_permission(self):
        return redirect('webapp:403')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['search_form'] = SearchForm(self.request.GET)
        return context


class UserPasswordChangeView(UserPassesTestMixin, PasswordChangeView):
    template_name = 'user_password_change.html'

    def test_func(self):
        return self.request.user.pk == self.kwargs.get('pk')

    def handle_no_permission(self):
        return redirect('webapp:403')

    def get_success_url(self):
        return reverse('accounts:profile', kwargs={'pk': self.request.user.pk})

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['search_form'] = SearchForm(self.request.GET)
        return context


class SearchResultView(ListView):
    model = User_model
    template_name = 'users_list.html'
    context_object_name = 'user_obj'
    paginate_by = 10
    paginate_orphans = 1
    ordering = ('username',)

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.search_form.is_valid():
            return self.search_form.cleaned_data['search']
        return None

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('webapp:403')
        self.search_form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(
                Q(username__icontains=self.search_value) |
                Q(email__icontains=self.search_value) |
                Q(first_name__icontains=self.search_value)
            )
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['search_form'] = self.search_form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search_value'] = self.search_value
        return context
