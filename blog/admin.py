from django.contrib import admin
from blog.models import Post

class ListPosts(admin.ModelAdmin):
    list_display = ('id','title','excerpt','published', )
    list_display_links = ('id','published','title', 'excerpt' )
    search_fields = ('title',)

admin.site.register(Post,ListPosts)
