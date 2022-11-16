from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Post(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='static/images/',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Post'
    
    def __str__(self):
        return self.title
    

class AboutUs(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=500)

    class Meta:
        verbose_name = 'AboutUs'
        verbose_name_plural = 'AboutUs'
    def __str__(self):
        return self.title


class Footer(models.Model):
    address = models.TextField(max_length=500)
    contact = PhoneNumberField(blank=True,null=True)
    facebook_link = models.URLField(blank=True,null=True)
    instagram_link = models.URLField(blank=True,null=True)
    twitter_link = models.URLField(blank=True,null=True)

    class Meta:
        verbose_name = 'Footer'
        verbose_name_plural = 'Footer'
    def __str__(self):
        return self.address


class SubscribedUsers(models.Model):
    email = models.EmailField(unique=True,max_length=100,null=True,blank=True)
    name = models.CharField(max_length=50,null=True,blank=True)

    class Meta:
        verbose_name = 'SubscribedUsers'
        verbose_name_plural = 'SubscribedUsers'

    def __str__(self):
        return str(self.email)


class ContactUs(models.Model):
    email = models.EmailField(unique=True,max_length=100,null=True,blank=True)
    message = models.TextField(blank=True,null=True,max_length=500)

    class Meta:
        verbose_name = 'ContactUs'
        verbose_name_plural = 'ContactUs'

    def __str__(self):
        return str(self.email)