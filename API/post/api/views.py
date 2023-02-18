from ..models import Post
from django.shortcuts import get_object_or_404
from .serializers import PostSerializer
from rest_framework import status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        post_queryset = Post.objects.all()
        count = post_queryset.count()
        serializer = PostSerializer(post_queryset, many=True)
        content = {"count": count, "data": serializer.data}
        return Response(content,  status=status.HTTP_200_OK)
    elif request.method == 'POST':
        print(request)
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        s
        return Response('ok')


@api_view(['GET', 'PATCH'])
def post_detail(request, **kwargs):
    pk = kwargs.get('pk')
    print(pk)
    post = get_object_or_404(Post, id=pk)
    if request.method == 'GET':
        serializer = PostSerializer(post)
        content = {
            'msg': f'post with title {post.title}', 'data': serializer.data}
        return Response(content, status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        serializer = PostSerializer(instance=post, data=request.data)
        serializer.is_valid(raise_exception=True)
        content = {
            "msg": f'post with title {post.title} has been updated', 'data': serializer.data}
        return Response(content, status=status.HTTP_201_CREATED)
