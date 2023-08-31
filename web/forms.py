from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class MyUserForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'email', 'username']

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = '__all__'
        
class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '4',
            'id': 'content',
            'placeholder' : 'Write your Comment for this post',
        }))
    class Meta:
        model = Comment
        fields = ('content',)
        
class AnnouceForm(ModelForm):
    class Meta:
        model = Annouce
        fields = '__all__'
        
class Comment1Form(forms.ModelForm):
    content = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '4',
            'id': 'content',
            'placeholder' : 'Write your Comment for this annoucement',
        }))
    class Meta:
        model = Comment1
        fields = ('content',)
        
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        
class ConstitutionForm(ModelForm):
    class Meta:
        model = Constitution
        fields = '__all__'
        
class MyfileForm(ModelForm):
    class Meta:
        model = Myfile
        fields = '__all__'

class SubscribeForm(ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__' 
        