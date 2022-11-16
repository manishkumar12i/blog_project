from django.contrib import admin
from blog.models import Post,AboutUs,Footer,SubscribedUsers,ContactUs,Idcreator

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


@admin.register(SubscribedUsers)
class SubscribedUsersModelAdmin(admin.ModelAdmin):
    list_display = ['id','email','name']
    list_filter = ['email']


@admin.register(ContactUs)
class ContactUsModelAdmin(admin.ModelAdmin):
    list_display = ['id','email','message']
    list_filter = ['email']


@admin.register(Idcreator)
class IdCreatorModelAdmin(admin.ModelAdmin):
    list_display = ['user_id']
    list_filter = ['user_id']