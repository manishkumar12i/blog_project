from django.shortcuts import render


def home(request):
    return render(request, 'blog/home.html' )

def about(request):
    return render(request, 'blog/about.html' )

def contact(request):
    return render(request, 'blog/contact.html' )

def login(request):
    return render(request, '/home/manish/Desktop/blog_project/miniblog/blog/templates/blog/login .html' )

def signup(request):
    return render(request, 'blog/signup.html' )

def dashboard(request):
    return render(request, 'blog/dashboard.html' )