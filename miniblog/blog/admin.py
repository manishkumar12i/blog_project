from django.contrib import admin
from blog.models import Post,AboutUs,Footer,SubscribedUsers,ContactUs,Set_Password

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
    list_display = ['id','email']
    list_filter = ['email']


@admin.register(ContactUs)
class ContactUsModelAdmin(admin.ModelAdmin):
    list_display = ['id','email','message']
    list_filter = ['email']



@admin.register(Set_Password)
class ContactUsModelAdmin(admin.ModelAdmin):
    list_display = ['id','new_password_1']
    list_filter = ['new_password_1']
