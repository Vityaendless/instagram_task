# Generated by Django 5.0.6 on 2024-06-01 14:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_alter_subscription_subscriber'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('text', models.TextField(max_length=400, verbose_name='Comment')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='webapp.publication', verbose_name='Comment')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
