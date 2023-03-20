from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from blog.forms import SignUpForm, LoginForm, PostForm,Pswrd_ResetForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from blog.models import Post, AboutUs, Footer, SubscribedUsers, ContactUs
from django.core.paginator import Paginator
from django.contrib.auth.models import Group, User
import re
from django.db.models import Q
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
import random
import math
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode , urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes,force_str
from django.core.exceptions import ValidationError



# generate otp for email


def generate_otp():
    numbers = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += numbers[math.floor(random.random()*10)]
    return OTP

# for home page


def home(request):
    posts = Post.objects.all().order_by('id')
    footer = Footer.objects.filter().first()
    return render(request, 'blog/home.html', {'posts': posts, 'footer': footer},)

# for about page


def about(request):
    about_obj = AboutUs.objects.filter().first()
    title = about_obj.title
    desc = about_obj.description
    footer = Footer.objects.filter().first()
    context = {
        'title': title,
        'desc': desc,
        'footer': footer,
    }
    return render(request, 'blog/about.html', context)

# for contact page


@csrf_exempt
def contact(request):
    footer = Footer.objects.filter().first()
    if request.method == "POST" or None:
        post_data = request.POST.copy()
        email = post_data.get("email")
        message = post_data.get("message")
        contactUs = ContactUs()
        try:
            contactUs.email = email
            contactUs.message = message
            contactUs.save()
            messages.success(request, 'Thanks for contact us:)')
        except IntegrityError:
            return HttpResponse('Email already used.Please Go back to previous page.')
    return render(request, 'blog/contact.html', {'footer': footer})

# for login page


@csrf_exempt
def user_login(request):
    footer = Footer.objects.filter().first()
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                human = True
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(
                    username=uname, password=upass, captcha=human)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully:)')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, 'blog/login .html', {'form': form, 'footer': footer})
    else:
        return HttpResponseRedirect('/dashboard/')


# for logout page
def user_logout(request):
    logout(request)
    messages.success(request, 'Logout Successfully:)')
    return HttpResponseRedirect('/')


# for sign up page
def user_signup(request):
    footer = Footer.objects.filter().first()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            messages.success(request, f'Registered Successfully:)')
            user = form.save()
            group = Group.objects.get(name="Author")
            user.groups.add(group)
            form = SignUpForm()
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form': form, 'footer': footer})


# hash generator function that prints hash with last name

# for dashboard page
def dashboard(request):
    footer = Footer.objects.filter().first()
    if request.user.is_authenticated:
        posts = Post.objects.all()
        paginator = Paginator(posts, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        user = request.user
        full_name = user.get_full_name()
        email = user.email
        gps = user.groups.all()
        short_name = user.last_name

        def fun(short_name):
            return ('#'+short_name)
        return render(request, 'blog/dashboard.html', {'posts': page_obj, 'full_name': full_name, 'groups': gps, 'email': email, 'page_obj': page_obj, 'last_name': fun(short_name), 'footer': footer})
    else:
        return HttpResponseRedirect('/login/')

# for add posts


@csrf_exempt
def add_post(request):
    footer = Footer.objects.filter().first()
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                title = form.cleaned_data['title']
                description = form.cleaned_data['description']
                photo = form.cleaned_data['photo']
                pst = Post(title=title, description=description, photo=photo)
                pst.save()
                messages.success(request, 'Post Added Successfully:)')
                form = PostForm()
                return HttpResponseRedirect('/dashboard/', {'form': form, 'footer': footer})
        else:
            form = PostForm()
        return render(request, 'blog/addpost.html', {'form': form, 'footer': footer})

    else:
        return HttpResponseRedirect('/login/')

# for update posts


@csrf_exempt
def update_post(request, id):
    footer = Footer.objects.filter().first()
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST, request.FILES, instance=pi)
            if form.is_valid():
                messages.success(request, 'Post Updated Successfully:)')
                form.save()
                return HttpResponseRedirect('/dashboard/')
        else:
            pi = Post.objects.get(pk=id)
            form = PostForm(instance=pi)
        return render(request, 'blog/updatepost.html', {'form': form, 'footer': footer})
    else:
        return HttpResponseRedirect('/login/')

# for delete post


@csrf_exempt
def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')


# for terms page
def terms(request):
    footer = Footer.objects.filter().first()
    return render(request, 'blog/terms.html', {'footer': footer})


# for search in home

def search(request):
    footer = Footer.objects.filter().first()
    if request.method == "GET":
        search = request.GET.get('search')
        if search == "":
            return HttpResponseRedirect('/')
        else:
            search = request.GET.get('search')
            post = Post.objects.all().filter(title__contains=search)
        return render(request, 'blog/search.html', {'post': post, 'footer': footer})


# for email subscription + email send
@csrf_exempt
def index(request):
    if request.method == 'POST':
        post_data = request.POST.copy()
        email = post_data.get("email", None)
        subscribedUsers = SubscribedUsers()
        subscribedUsers.email = email
        subscribedUsers.save()
        # send a confirmation mail
        subject = 'NewsLetter Subscription'
        message = 'Hello ' + \
            ', Thanks for subscribing us. You will get notification for posts. Please do not reply on this email.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(subject, message, email_from, recipient_list)
        res = JsonResponse(
            {'msg': 'You successfully subscribed our newsletter'})
        return res
    return HttpResponseRedirect('/')


@csrf_exempt
def validate_email(request):
    email = request.POST.get("email")
    if SubscribedUsers.objects.filter(email=email):
        res = JsonResponse({'msg': 'Email Address already exists'})
    elif email == "":
        res = JsonResponse({'msg': 'Email is required.'})
    elif not re.match(r"^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$", email):
        res = JsonResponse({'msg': 'Invalid Email Address'})
    else:
        res = JsonResponse({'msg': ''})
    return res


# otp used in email function
def otp_mail(request):
    email = request.POST.get("email")
    otp = generate_otp()
    htmltext = '<p>Your OTP is <strong>' + otp + \
        '</strong>Use this otp in user registration.</p>'
    email_from = settings.EMAIL_HOST_USER
    send_mail('OTP request for registered mail id :', otp, email_from, [
              email], fail_silently=False, html_message=htmltext)
    return HttpResponse(f'OTP is : {otp}')


# password reset
def password_reset_request(request):
    footer = Footer.objects.filter().first()
    if request.method == "POST":
        password_reset_form = Pswrd_ResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "blog/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com',
                                  [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return render(request,template_name="blog/password_reset_done.html",context={'footer':footer})
    psword_reset_form = Pswrd_ResetForm()
    return render(request=request, template_name="blog/password_reset.html", context={"password_reset_form": psword_reset_form, 'footer': footer})





def passwordResetConfirm(request, uidb64 , token):
    footer = Footer.objects.filter().first()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            new_password = request.POST.get("new_password1")
            confirm_new_password = request.POST.get("new_password2")
            if form.is_valid():
                form.save()
                return render(request,'blog/password_reset_complete.html',{'footer':footer})
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
            if new_password != confirm_new_password:
                data = [{
                    "message":"Please use same password as above."
                }]
                return JsonResponse(data,safe=False)
                
        form = SetPasswordForm(user)
        return render(request,'blog/password_reset_confirm.html',{'form':form,'footer':footer})
    else:
        messages.error(request, "Link is expired")
    form = SetPasswordForm(user)
    return render(request,template_name='blog/password_reset_confirm.html',context={'form':form ,'footer':footer})
