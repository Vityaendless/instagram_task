from django.contrib import admin

from .models import Publication, Subscription, Like, Comment


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'created_at']
    list_display_links = ['id', 'content']
    list_filter = ['content']
    search_fields = ['content', 'author']
    fields = [
        'content', 'author', 'img', 'likes_count',
        'comments_count', 'updated_at', 'created_at'
    ]
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['id']
    list_display_links = ['id']
    fields = ['user', 'subscriber']


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id']
    list_display_links = ['id']
    fields = ['user', 'publication']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id']
    list_display_links = ['id']
    fields = [
        'publication', 'text', 'author',
        'updated_at', 'created_at'
    ]
    readonly_fields = ['created_at', 'updated_at']
