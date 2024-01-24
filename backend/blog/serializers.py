from rest_framework import serializers

from .models import Blog, Note

class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

        
class BlogListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'



# class BlogDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Blog
#         fields = ('id', 'title', 'content', 'slug')


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
