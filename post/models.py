from django.db import models

from datetime import datetime
class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    thumb = models.ImageField(upload_to="images/%Y/%m/%d", blank=True)
    excerpt = models.TextField(max_length=200)
    body = models.TextField()
    slug = models.SlugField()
    post_date = models.DateTimeField(default=datetime.now)
    published  = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    # thumb = 
    # author = 

