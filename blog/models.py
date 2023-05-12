from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    excerpt = models.TextField(max_length=200)

    def __str__(self):
        return f'Post [title={self.title}]'
    # thumb = 
    # author = 
