from django.db import models
from django.contrib.auth.models import AbstractUser


gender_choices = [('m', 'Man'), ('w', 'Woman')]


class AppUser(AbstractUser):
    email = models.EmailField(max_length=30, null=False, blank=False, verbose_name="Email")
    avatar = models.ImageField(upload_to='user_pics', verbose_name='Avatar')
    bio = models.TextField(max_length=3000, null=True, blank=True, verbose_name="Bio")
    phone = models.CharField(max_length=15, null=True, blank=True, verbose_name="Phone number")
    gender = models.CharField(max_length=30, null=True, blank=True, verbose_name='Gender', choices=gender_choices)
