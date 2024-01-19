import email
from email.policy import default
from django.db import models
from django.db import models
from froala_editor.fields import FroalaField
from django.utils.timezone import timezone
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user     = models.ForeignKey(User,on_delete=models.CASCADE)
    is_verified  = models.BooleanField(default=False)
    token        = models.CharField(max_length=100)

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published')
    )
    title = models.CharField(max_length=200)
    slug  = models.SlugField(max_length=200)
    body  = FroalaField()
    image   = models.ImageField(upload_to='uploads')
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)
    status  = models.CharField(choices=STATUS_CHOICES,default='draft',max_length=10)
    publish = models.DateTimeField(default=timezone.now())
    author  = models.ForeignKey(User,on_delete=models.CASCADE,
                                related_name='posted')
    objects   = models.Manager()  #Default Manager
    published = PublishedManager() #Custom Manager
    
    
    def __str__(self):
        return self.title 


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name="comments")
    username = models.CharField(max_length=100)
    email    = models.EmailField(max_length=200)
    body     = models.TextField()
    created  = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True)
    
    
    def  __str__(self):
        return self.post.title
    


  
class Membres(models.Model):
    
    nom = models.ForeignKey(User,on_delete=models.CASCADE,related_name='membre')
    
    role = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='uploads',default='')
    upload_to = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.role
    

class Partenaire(models.Model):
    
    nom = models.CharField(max_length=200)
    image   = models.ImageField(upload_to='uploads')
    upload_to = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.nom 
