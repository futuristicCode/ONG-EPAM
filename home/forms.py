from django import forms
from froala_editor.widgets import FroalaEditor
from .models import *
from  .models import Comment
from django.contrib.auth.models import User

from dataclasses import fields
from django  import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Username',max_length=250,help_text='',required=True,
                               widget=forms.TextInput(attrs={"class":"form-control","id":"username","type":"text","placeholder":"Utilisateur","data-sb-validations":"required"}))
    
    first_name = forms.CharField(label='nom',max_length=250,help_text='',required=True,
                               widget=forms.TextInput(attrs={"class":"form-control","id":"nom","type":"text","placeholder":"Nom","data-sb-validations":"required"}))
    
    last_name = forms.CharField(label='prenom',max_length=250,min_length=3,help_text='',required=True,
                               widget=forms.TextInput(attrs={"class":"form-control","id":"prenom","type":"text","placeholder":"Prenom","data-sb-validations":"required"}))

    password = forms.CharField(label='password',max_length=250,min_length=8,help_text='',required=True,
                               widget=forms.TextInput(attrs={"class":"form-control","id":"password","type":"password","placeholder":"Mot de passe","data-sb-validations":"required"}))
    
    confirmer = forms.CharField(label='confirmer',max_length=250,min_length=8,help_text='',required=True,
                               widget=forms.TextInput(attrs={"class":"form-control","id":"confirmer","type":"password","placeholder":"Confirmer","data-sb-validations":"required"}))
    
    email = forms.EmailField(label='Email',max_length=250,min_length=5,help_text='',required=True,
                               widget=forms.TextInput(attrs={"class":"form-control","id":"emailAddress","type":"email","placeholder":"Email ","data-sb-validations":"required,email"}))
    
    class Meta:
        model   = User
        fields  = ('first_name','last_name', 'email','username',)

class PostForm(forms.ModelForm):
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published')
    )
    title  = forms.CharField(max_length=200,widget=forms.TextInput(attrs={"class":"form-control","type":"text","placeholder":"Entre le titre","name":"title"}))
    status = forms.ChoiceField(choices=STATUS_CHOICES,widget=forms.Select(attrs={"class":"form-select","type":"select","name":"status"}))
    # author = forms.ChoiceField(choices=User,widget=forms.Select(attrs={"class":"form-select","type":"select","name":"author"}))
    # image   = forms.ImageField(widget=forms.FileField(attrs={"class":"form-control","type":"file","name":"image","id":"formFile"}))
    
    class Meta:
        model = Post
        fields = ['title','body','status','author','image',] 

class CommentForm(forms.ModelForm):
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    email    = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    body     = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','row':3}))
    class Meta:
        model  = Comment
        fields = ['username','email','body'] 