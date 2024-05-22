# Generated by Django 5.0.6 on 2024-05-22 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='publications',
            field=models.IntegerField(default=0, verbose_name='Publications'),
        ),
        migrations.AddField(
            model_name='appuser',
            name='subscribers',
            field=models.IntegerField(default=0, verbose_name='Subscribers'),
        ),
        migrations.AddField(
            model_name='appuser',
            name='subscriptions',
            field=models.IntegerField(default=0, verbose_name='Subscriptions'),
        ),
    ]
