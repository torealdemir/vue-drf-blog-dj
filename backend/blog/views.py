from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import BlogListSerializer, BlogListCreateSerializer

from .models import Blog

from rest_framework import viewsets
from rest_framework import status

from rest_framework.response import Response
from rest_framework.parsers import (MultiPartParser, FormParser)
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class BlogCreateAPIView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes=[MultiPartParser, FormParser]
    

    def post(self, request):
        serializer = BlogListCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)  # Set the created_by field to the current user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_blogd(request, slug):
    blogd = Blog.objects.get(slug=slug)
    serializer = BlogListSerializer(blogd)
    return Response(serializer.data)

class BlogListViewset(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogListSerializer


class BlogDeleteApiView(generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class=BlogListCreateSerializer
    