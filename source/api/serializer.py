from rest_framework import serializers
from webapp.models import Publication


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = [
            'id', 'img', 'content', 'author',
            'likes_count', 'comments_count',
            'created_at', 'updated_at'
        ]
        read_only_fields = [
            'likes_count', 'comments_count', 'created_at',
            'updated_at', 'author'
        ]
