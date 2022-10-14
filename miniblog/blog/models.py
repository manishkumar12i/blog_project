from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    photo = models.ImageField(upload_to='static/images/',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Post'
    
    def __str__(self):
        return self.title
    

class AboutUs(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)

    class Meta:
        verbose_name = 'AboutUs'
        verbose_name_plural = 'AboutUs'
    def __str__(self):
        return self.title
