from django.contrib import admin
from post.models import Post
from .forms import PostAdminForm

class ListPosts(admin.ModelAdmin):
    list_display = ('id','title','excerpt','published', )
    list_display_links = ('id','published','title', 'excerpt' )
    search_fields = ('title',)
    form = PostAdminForm



admin.site.register(Post,ListPosts)
