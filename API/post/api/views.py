from ..models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
from rest_framework.decorators import action


class PostViewset(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_serializer_context(self):
        return self.request

    @action(methods=['post'], detail=True)
    def like_post(self, request, **kwargs):
        post = self.get_object()
        pass
