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