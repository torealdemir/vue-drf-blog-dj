from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import BlogListSerializer, BlogDetailSerializer

from .models import Blog


@api_view(['GET'])
def get_blogs(request):
    blogs = Blog.objects.all()
    serializer = BlogListSerializer(blogs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_blogd(request, slug):
    blogd = Blog.objects.get(slug=slug)
    serializer = BlogDetailSerializer(blogd)
    return Response(serializer.data)


