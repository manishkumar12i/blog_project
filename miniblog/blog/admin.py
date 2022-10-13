from django.contrib import admin
from blog.models import Post

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','description']
    list_filter = ['title']
    
