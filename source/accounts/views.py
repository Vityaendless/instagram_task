from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .auth import EmailUsernameAuthentication as EUA


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
