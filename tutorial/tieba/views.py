from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework import status
from .models import Post, TestPage
from .serializers import PostSerializer, TestPageSerializer
from .permissions import IsPostAuthor
from rest_framework.response import Response
from django.http import HttpResponse, Http404
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from rest_framework import request


class TestPagination(PageNumberPagination):
    page_size = 10
    pass


class TestPageList(APIView):
    queryset = TestPage.objects.all()
    serializer_class = TestPageSerializer
    pagination_class = TestPagination

    def get(self, request):
        pagination = self.pagination_class()
        objs = pagination.paginate_queryset(request=request, queryset=TestPage.objects.all())
        serializer = self.serializer_class(objs, many=True)
        return Response(status=200, data=serializer.data)


class PostList(APIView):
    """
    List all tieba, or create a new post
    """
    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailView(APIView):
    # authentication_classes = (TokenAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated, IsPraiseAuthor)
    permission_classes = (IsPostAuthor,)

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        # self.check_object_permissions(request, post)
        self.check_object_permissions(request, post)
        serializer = PostSerializer(post)
        return Response(status=200, data=serializer.data)

    def delete(self, request, pk, *args, **kwargs):
        post = self.get_object(pk)
        self.check_object_permissions(request, post)
        post.delete()
        return Response(status=201)
