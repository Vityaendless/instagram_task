# Generated by Django 5.0.6 on 2024-05-26 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_appuser_publications_appuser_subscribers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='email',
            field=models.EmailField(max_length=30, unique=True, verbose_name='Email'),
        ),
    ]
