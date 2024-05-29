from django.views.generic import View
from django.shortcuts import redirect, reverse, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin
from ..models import Subscription


class SubscriptionCreateView(View):
    def get(self, request, *args, **kwargs):
        user = self.request.user
        subscriber = get_object_or_404(get_user_model(), pk=kwargs.get('pk'))
        Subscription.objects.create(user=user, subscriber=subscriber)
        request.user.increase_count('subscriptions')
        subscriber.increase_count('subscribers')
        return redirect('accounts:profile', pk=subscriber.pk)

    # def test_func(self):
    #     return self.request.user.pk == self.kwargs.get('pk')
    #
    # def handle_no_permission(self):
    #     return redirect('webapp:403')


    #пермишены = не должен иметь возможности по юрлу подписать сам на себя
    #ссылка на лист подписок или на лист подписантов = по кнопке удаление
    #нельзя повторно подписаться - заделать это в пермишены????
    #На главной странице пользователя показывать публикации его подписок, отсортированные в порядке по убыванию (сначала самые новые)


