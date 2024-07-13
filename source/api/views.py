from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS

from .serializer import PublicationSerializer
from .permissions import IsAuthorPermission
from webapp.models import Publication, Like


class LogoutView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            user.auth_token.delete()
        return Response({'status': 'ok'})



class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        elif self.action in ('like', 'unlike'):
            return [IsAuthenticated()]
        else:
            return [IsAuthorPermission()]

    @action(detail=True, methods=['POST'], url_path='like')
    def like(self, request, *args, **kwargs):
        user = request.user
        publication = self.get_object()
        like = Like.objects.filter(user=user, publication=publication)
        if not like:
            Like.objects.create(user=user, publication=publication)
            publication.increase_count('likes')
        return Response({'likes_count': publication.likes_count})

    @action(detail=True, methods=['DELETE'], url_path='unlike')
    def unlike(self, request, *args, **kwargs):
        user = request.user
        publication = self.get_object()
        like = Like.objects.filter(user=user, publication=publication)
        if like:
            like.delete()
            publication.likes_count -= 1
            publication.save()
        return Response({'likes_count': publication.likes_count})
