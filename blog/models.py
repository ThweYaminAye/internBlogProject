from django.db import models
from django.contrib.auth.models import User

STATUS = ((0,'Draft'),(1,'Publish'),(2,'Editing'))
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(max_length=50,unique=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True)
    status = models.IntegerField(choices=STATUS,default=2)

    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return self.title


class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='images/')

    def __str__(self):
        return self.post.title


