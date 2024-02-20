from rest_framework import serializers
from PIL import Image
from io import BytesIO
from .models import Blog
from django.core.files.uploadedfile import InMemoryUploadedFile

class BlogListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = Blog
        fields = ['id', 'title', 'slug', 'short_description', 'created_at', 'updated_at', 'content', 'created_by_username', 'image']
    
    def get_image(self, Blog):
        if Blog.image:
            return Blog.image.url
        return None
    

        
class BlogListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

    def to_internal_value(self, data):
        file_data = data.get('image')

        if file_data:
            file_name = file_data.name
            image = self.resize_image(file_data)
            file_data = self.create_uploaded_file(image, file_name)
            data['image'] = file_data

        return super().to_internal_value(data)

    def resize_image(self, image):
        pil_image = Image.open(image)

        resized_image = pil_image.resize((250, 250)) 

        output = BytesIO()
        resized_image.save(output, format='JPEG') 
        output.seek(0)

        return output

    def create_uploaded_file(self, file, filename):
        uploaded_file = InMemoryUploadedFile(
            file, 
            None, 
            filename,  
            'image/jpeg', 
            file.getbuffer().nbytes,  
            None 
        )

        return uploaded_file