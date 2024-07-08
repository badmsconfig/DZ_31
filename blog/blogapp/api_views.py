from rest_framework import viewsets

from .models import Category, Post, Tag
from .serializers import CategorySerializer, PostSerializer, TagSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from .permissions import ReadOnly, IsAutor


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser|ReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser|IsAutor|ReadOnly]
    queryset = Post.objects.prefetch_related('tags')
    serializer_class = PostSerializer

class TagViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer