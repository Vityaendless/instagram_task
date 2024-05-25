from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, get_user_model
from django.views.generic import DetailView, UpdateView
from .auth import EmailUsernameAuthentication as EUA
from .forms import UserForm


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


class UserUpdateView(UpdateView):
    template_name = 'edit_profile.html'
    model = User_model
    form_class = UserForm
