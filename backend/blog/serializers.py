from rest_framework import serializers

from .models import Blog

class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'slug', 'short_description', 'created_at', 'updated_at', 'content', 'created_by_username']
        
class BlogListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
