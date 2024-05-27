from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout, get_user_model
from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import UserPassesTestMixin
from .auth import EmailUsernameAuthentication as EUA
from .forms import UserForm
from django.core.exceptions import PermissionDenied


User_model = get_user_model()


def login_view(request):
    context = {}
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


class RegisterView(CreateView):
    model = get_user_model()
    form_class = UserForm
    template_name = 'registration.html'

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


class UserPasswordChangeView(UserPassesTestMixin, PasswordChangeView):
    template_name = 'user_password_change.html'

    def test_func(self):
        return self.request.user.pk == self.kwargs.get('pk')

    def handle_no_permission(self):
        return redirect('webapp:403')

    def get_success_url(self):
        return reverse('accounts:profile', kwargs={'pk': self.request.user.pk})
