from django.views.generic import View
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView

from ..models import Subscription, Publication
from ..forms import SearchForm
from accounts.views import User_model


class SubscriptionCreateView(View):
    def get(self, request, *args, **kwargs):
        user = self.request.user
        subscriber = get_object_or_404(User_model, pk=kwargs.get('pk'))
        subscribe = Subscription.objects.filter(user=user, subscriber=subscriber)
        if not subscribe and user != subscriber:
            Subscription.objects.create(user=user, subscriber=subscriber)
            request.user.increase_count('subscriptions')
            subscriber.increase_count('subscribers')
        return redirect('accounts:profile', pk=subscriber.pk)


class SubscribersListView(ListView):
    model = User_model
    template_name = 'subscribition/subscribers.html'
    context_object_name = 'user_obj'
    paginate_by = 10
    paginate_orphans = 1
    ordering = ('username',)

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('webapp:403')
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        user = get_object_or_404(User_model, pk=self.kwargs.get('pk'))
        subscribe = Subscription.objects.filter(subscriber=user)
        if subscribe:
            subscribitions_pk = []
            for subscribition in subscribe:
                subscribitions_pk.append(subscribition.user.pk)
            queryset = queryset.filter(pk__in=subscribitions_pk)
        else:
            queryset = []
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['search_form'] = SearchForm(self.request.GET)
        return context


class SubscribitionsListView(ListView):
    model = User_model
    template_name = 'subscribition/subscribitions.html'
    context_object_name = 'user_obj'
    paginate_by = 10
    paginate_orphans = 1
    ordering = ('username',)

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('webapp:403')
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        user = get_object_or_404(User_model, pk=self.kwargs.get('pk'))
        subscribe = Subscription.objects.filter(user=user)
        if subscribe:
            subscribitions_pk = []
            for subscribition in subscribe:
                subscribitions_pk.append(subscribition.subscriber.pk)
            queryset = queryset.filter(pk__in=subscribitions_pk)
        else:
            queryset = []
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['search_form'] = SearchForm(self.request.GET)
        return context
