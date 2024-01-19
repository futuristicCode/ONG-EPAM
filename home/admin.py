from distutils.errors import PreprocessError
from re import search
from django.contrib import admin
from .models import Membres, Partenaire, Post,Comment, Profile

# Register your models here.
#admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display        = ('title','created_at','status','author','publish')
    prepopulated_fields = {'slug':('title',)}
    search_fields       = ('title','body')
    ordering            = ('author','status','publish')
    list_filter         = ('author','created_at','publish')

@admin.register(Comment)
class Comments(admin.ModelAdmin):
    list_display  = ['username','email','created']
    
@admin.register(Membres)
class MembreAdmin(admin.ModelAdmin):
    list_display        = ('nom','role')
    
@admin.register(Partenaire)
class PartenaireAdmin(admin.ModelAdmin):
    list_display        = ('nom',)
    
@admin.register(Profile)
class PartenaireAdmin(admin.ModelAdmin):
    list_display        = ('user',)
