from django.forms import SlugField
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import BlogListSerializer, NoteSerializer, BlogListCreateSerializer

from .models import Blog, Note

from rest_framework import viewsets
from rest_framework import permissions, status
from rest_framework.views import APIView











from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class BlogCreateAPIView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    

    def post(self, request):
        serializer = BlogListCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)  # Set the created_by field to the current user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





# class BlogCreateAPIView(APIView):
#     def post(self, request):
#         serializer = BlogListCreateSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(created_by=request.user)  # Set the created_by field to the current user
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_blogs(request):
    blogs = Blog.objects.all()
    serializer = BlogListSerializer(blogs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_blogd(request, slug):
    blogd = Blog.objects.get(slug=slug)
    serializer = BlogListSerializer(blogd)
    return Response(serializer.data)

# @api_view(['POST'])
# def add_blog(request):
#     # data = request.data
#     # title = Blog.objects.get(title=title)
#     # content = Blog.objects.get(long_description = content)

#     blog = Blog.objects.create(
#         title=request.data.get('title'),
#         content=request.data.get('long_description')
#     )

#     blog.save()


# def createNote(request):
#     data=request.data
#     note=Note.objects.create(
#         body=data['content'],
#         title=data['title']
#     )
#     serializer = NoteSerializer(note, many=False)
#     return Response(serializer.data)
    
class NoteViewset(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class BlogListViewset(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogListSerializer

class BlogDetailViewset(viewsets.ModelViewSet):
    queryset = Blog.objects.filter(slug=id)
    serializer_class = BlogListCreateSerializer

# class BlogCreateViewset(viewsets.ModelViewSet): 
#     queryset = Blog.objects.create()
#     serializer_class = BlogListSerializer
#     permission_classes = permissions.AllowAny
    