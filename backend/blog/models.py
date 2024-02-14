from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(null=True)
    short_description = models.TextField(blank=True, null = True)
    created_at = models.DateField(auto_now_add = True, null = True)
    updated_at = models.DateField(auto_now= True)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete= models.CASCADE, null = True)
    
    def __str__(self):
        return self.title
    


