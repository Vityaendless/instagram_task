from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser


gender_choices = [('m', 'Man'), ('w', 'Woman')]


class AppUser(AbstractUser):
    email = models.EmailField(max_length=30, unique=True, null=False, blank=False, verbose_name="Email")
    avatar = models.ImageField(upload_to='user_pics', verbose_name='Avatar')
    bio = models.TextField(max_length=3000, null=True, blank=True, verbose_name="Bio")
    phone = models.CharField(max_length=15, null=True, blank=True, verbose_name="Phone number")
    gender = models.CharField(max_length=30, null=True, blank=True, verbose_name='Gender', choices=gender_choices)
    publications_count = models.IntegerField(default=0, verbose_name='Publications')
    subscriptions_count = models.IntegerField(default=0, verbose_name='Subscriptions')
    subscribers_count = models.IntegerField(default=0, verbose_name='Subscribers')

    def increase_count(self, marker):
        match marker:
            case 'publications':
                self.publications_count += 1
            case 'subscriptions':
                self.subscriptions_count += 1
            case 'subscribers':
                self.subscribers_count += 1
        self.save()

    def __str__(self):
        return f'{self.first_name} {self.last_name}, username: {self.username}'

    def get_absolute_url(self):
        return reverse('accounts:profile', kwargs={'pk': self.pk})
