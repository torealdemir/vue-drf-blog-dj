from rest_framework import serializers

from .models import Blog

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

