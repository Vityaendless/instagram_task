# Generated by Django 5.0.6 on 2024-05-29 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_appuser_publications_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appuser',
            old_name='subscribers',
            new_name='subscribers_count',
        ),
        migrations.RenameField(
            model_name='appuser',
            old_name='subscriptions',
            new_name='subscriptions_count',
        ),
    ]
