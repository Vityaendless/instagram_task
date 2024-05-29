# Generated by Django 5.0.6 on 2024-05-29 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publication',
            old_name='comments',
            new_name='comments_count',
        ),
        migrations.RenameField(
            model_name='publication',
            old_name='likes',
            new_name='likes_count',
        ),
        migrations.AlterField(
            model_name='publication',
            name='content',
            field=models.TextField(max_length=3000, verbose_name='Content'),
        ),
    ]
