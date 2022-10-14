from django.contrib import admin
from blog.models import Post,AboutUs

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','description']
    list_filter = ['title']
    

@admin.register(AboutUs)
class AboutUsModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','description']
    list_filter = ['title']
    