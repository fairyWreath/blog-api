from rest_framework import generics
# drf has its own permissions layer
# permissions can go from project level to any view level
# examples are AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

from .serializers import PostSerializer
from .models import Post
from .permissions import IsAuthorOrReadOnly

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer



