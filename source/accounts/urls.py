from django.urls import path
from .views import (login_view, logout_view, UserView,
                    RegisterView, UserUpdateView, UserPasswordChangeView)


app_name = 'accounts'


urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/<int:pk>/', UserView.as_view(), name='profile'),
    path('registration/', RegisterView.as_view(), name='registration'),
    path('profile/<int:pk>/update', UserUpdateView.as_view(), name='edit_profile'),
    path('profile/<int:pk>/password_change/', UserPasswordChangeView.as_view(), name='user_password_change'),
]
