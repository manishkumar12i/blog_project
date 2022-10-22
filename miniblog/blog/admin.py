from django.contrib import admin
from blog.models import Post,AboutUs,Footer,Email

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','description']
    list_filter = ['title']
    

@admin.register(AboutUs)
class AboutUsModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','description']
    list_filter = ['title']
    

@admin.register(Footer)
class FooterModelAdmin(admin.ModelAdmin):
    list_display = ['id','address','contact','facebook_link','instagram_link','twitter_link']
    list_filter = ['address']


@admin.register(Email)
class EmailModelAdmin(admin.ModelAdmin):
    list_display = ['id','email']
    list_filter = ['email']