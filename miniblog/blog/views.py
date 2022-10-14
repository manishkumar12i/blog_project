from django.shortcuts import render
from django.http import HttpResponseRedirect
from blog.forms import SignUpForm, LoginForm, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from blog.models import Post
from django.core.paginator import Paginator
from django.contrib.auth.models import Group


def home(request):
    posts = Post.objects.all().order_by('id')
    return render(request, 'blog/home.html', {'posts': posts})


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    return render(request, 'blog/contact.html')


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully:)')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, '/home/manish/Desktop/blog_project/miniblog/blog/templates/blog/login .html', {'form': form})
    else:
        return HttpResponseRedirect('/dashboard/')


def user_logout(request):
    logout(request)
    messages.success(request, 'Logout Successfully:(')
    return HttpResponseRedirect('/')


def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            messages.success(request, 'Registered Successfully:)')
            user = form.save()
            group = Group.objects.get(name="Author")
            user.groups.add(group)

    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form': form})


def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        paginator = Paginator(posts,5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        user = request.user
        full_name = user.get_full_name()
        email = user.email
        gps = user.groups.all()
        return render(request, 'blog/dashboard.html', {'posts': page_obj,'full_name':full_name,'groups':gps,'email':email,'page_obj':page_obj})
    else:
        return HttpResponseRedirect('/login/')

# for add posts


def add_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST , request.FILES)
            if form.is_valid():
                title = form.cleaned_data['title']
                description = form.cleaned_data['description']
                photo = form.cleaned_data['photo']
                pst = Post(title=title, description=description,photo=photo)
                pst.save()
                messages.success(request,'Post Added Successfully:)')
                form = PostForm()
                return HttpResponseRedirect('/dashboard/',{'form':form})
        else:
            form = PostForm()
        return render(request, 'blog/addpost.html', {'form': form})

    else:
        return HttpResponseRedirect('/login/')

# for update posts


def update_post(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST, request.FILES, instance=pi)
            if form.is_valid():
                messages.success(request,'Post Updated Successfully:)')
                form.save()
                return HttpResponseRedirect('/dashboard/')
        else:
            pi = Post.objects.get(pk=id)
            form = PostForm(request.FILES,instance=pi)
        return render(request, 'blog/updatepost.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')

# for delete post


def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')
