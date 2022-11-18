from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from blog .models import Post
from django.utils.translation import gettext,gettext_lazy as _
from captcha.fields import CaptchaField

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'first_name':'First Name','last_name':'Last Name','email':'Email','username':'User Name'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),'first_name':forms.TextInput(attrs={'class':'form-control'}),'last_name':forms.TextInput(attrs={'class':'form-control'}),'email':forms.TextInput(attrs={'class':'form-control'})}


class LoginForm(AuthenticationForm):
    captcha = CaptchaField()
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_("Password"),strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','description','photo']
        labels = {'title':'Title','description':'Description','photo':'Upload Image'}
        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),'description':forms.Textarea(attrs={'class':'form-control'})}