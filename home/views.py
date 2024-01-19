from multiprocessing import context
from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from home.forms import CommentForm
from home.models import Post,Membres,Partenaire,Comment
from .models import Post,Membres,Partenaire,Comment
from  .forms import *
from django.contrib.auth import logout,authenticate
from rest_framework import permissions

# Create your views here.

def  register_view(request):
  if request.user.is_authenticated:
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('login_view')
        else:
            return render(request,'register.html',{'user_form':user_form})
    else:
        user_form = RegistrationForm()
        return render(request,'register.html',{'user_form':user_form })
  
  return redirect('/login/')

def logout_view(request):
  logout(request)
  return redirect('/')

def post_list(request):
    object_list = Post.published.all()
    paginator   = Paginator(object_list,6)
    page        = request.GET.get('page')
    
    try:
      posts = paginator.page(page)
    except PageNotAnInteger:
      posts = paginator.page(1)
    except EmptyPage:
      posts = Paginator.page(paginator.num_pages)
    context = {
      'posts':posts,
      'page' :page,
    }
    
    return render(request,'blog/post/liste.html',context)



def post_details(request ,slug:str):
    
  post      = get_object_or_404(Post,slug=slug)
  comments  = Comment.objects.filter(post=post.id)
  new_comment = None
  if request.method == 'POST':
    comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
      new_comment = comment_form.save(commit=False)
      new_comment.post = post
      new_comment.save()
  else: 
    comment_form = CommentForm()
  return render(request,'blog/post/details.html',{'post':post,'comments':comments,'new_comment':new_comment,'comment_form':comment_form}) 




def membre_list(request):
  
  object_list = Membres.objects.all()
  paginator   = Paginator(object_list,10)
  page        = request.GET.get('page')
    
  try:
    membres = paginator.page(page)
  except PageNotAnInteger:
    membres = paginator.page(1)
  except EmptyPage:
    membres = Paginator.page(paginator.num_pages)
  context = {
    'membres':membres,
    'page' :page,
  }
  
    
  return render(request,'blog/post/membres.html',context)



def partenaires_list(request):
  
  object_list = Partenaire.objects.all()
  paginator   = Paginator(object_list,10)
  page        = request.GET.get('page')
    
  try:
   partenaires = paginator.page(page)
  except PageNotAnInteger:
    partenaires = paginator.page(1)
  except EmptyPage:
    partenaires = Paginator.page(paginator.num_pages)
  context = {
    'partenaires':partenaires,
    'page' :page,
  }
  
    
  return render(request,'blog/post/services.html',context)


def login_view(request):
  return render(request, 'blog/auth/login.html',)


def register_view(request):
  if request.user.is_authenticated:
   return render(request, 'blog/auth/register.html',)
  return redirect('/login/')

def verify(request,token):
    try:
        profile_obj = Profile.objects.filter(token = token).first()
        
        if profile_obj:
            profile_obj.is_verified = True
            profile_obj.save()
        return redirect('/login/')

    except Exception as e : 
        print(e)
    
    return redirect('/')


def add_blog(request):
  if request.user.is_authenticated:
    context = {'form': PostForm}
    try:
       if request.method == 'POST':
          form = PostForm(request.POST)
          print(request.FILES)
          image = request.FILES['image']
          title = request.POST.get('title')
          body = request.POST.get('body')
          status= request.POST.get('status')
          author = request.user
            
          if form.is_valid():
            body = form.cleaned_data['body']
            
          blog_obj = Post.objects.create(
              author = author,title = title, 
              body = body, image = image,
              status = status,
            )
          print(blog_obj)
          return redirect('/add-blog/')
            
    except Exception as e :
     print(e)
      
    return render(request, 'blog/auth/add_blog.html',context)
  return redirect('/login/')

# def see_blog(request):
#   context = {}
#   try: 
#     blog_objs = Post.objects.all()
#     context['blog_objs'] = blog_objs
  
#   except Exception as e :
#     print(e)
    
#   print(context)
#   return render(request,'blog/auth/see_blog.html',context)

def see_blog(request):
  if request.user.is_authenticated:
    object_list = Post.objects.all()
    paginator   = Paginator(object_list,10)
    page        = request.GET.get('page')
    
    try:
      posts = paginator.page(page)
    except PageNotAnInteger:
      posts = paginator.page(1)
    except EmptyPage:
      posts = Paginator.page(paginator.num_pages)
    context = {
      'posts':posts,
      'page' :page,
    }
    
    return render(request,'blog/auth/see_blog.html',context)
  return redirect('/login/')



# def update_blog(request , slug):
#   context = {}
  
#   try:
            
#     blog_obj = Post.objects.get(slug = slug)
       
        
#     if blog_obj.author != request.user:
#       return redirect('/')
        
#     initial_dict = {'body': blog_obj.body}
#     form = Post(initial = initial_dict)
#     if request.method == 'POST':
#       form = Post(request.POST)
#       print(request.FILES)
#       image = request.FILES['image']
#       title = request.POST.get('title')
#       status= request.POST.get('status')
#       author = request.user
            
#         if form.is_valid():
#           body = form.cleaned_data['body']
            
#         blog_obj = Post.objects.create(
#           author = author,title = title, 
#           body = body, image = image,
#           status = status,
#           )
        
        
#     context['blog_obj'] = blog_obj
#     context['form'] = form
    
#     except Exception as e :
#     print(e)

#     return render(request , 'update_blog.html' , context)

def update_blog(request,pk):
  if request.user.is_authenticated:
    # context = {}
    context = {}
    try:
        
        
     # blog_obj = Post.objects.get(slug = slug)
     # blog_obj = Post.objects.get(id = pk)
      blog_obj = Post.objects.get(pk = pk)
    
    
    
      initial_dict = {'body':blog_obj.body,'title':blog_obj.title,'status':blog_obj.status,'author':blog_obj.author,'image':blog_obj.image}
      
      form = PostForm(initial=initial_dict)
        
      if request.method == 'POST':
        form = PostForm(request.POST)
        print(request.FILES)
        print(request.POST)
        image = request.FILES['image']
        title = request.POST.get('title')
        body = request.POST.get('body')
        status= request.POST.get('status')
        author = request.user
            
        if form.is_valid():
          # form.save()
          body = form.cleaned_data['body']
            
        blog_obj = Post.objects.update_or_create(
          author = author,title = title, 
          body = body, image = image,
          status = status,
          )
          
        return redirect('/see-blog/')
               
      context['blog_obj'] = blog_obj
      context['form'] = form
    
    except Exception as e :
      print(e)

    return render(request , 'blog/auth/update_blog.html' , context)
  return redirect('/login/')


def blog_delete(request,id):
  if request.user.is_authenticated:
    try:
      blog_obj  =  Post.objects.get(id = id)
    
      if blog_obj.author == request.user:
        blog_obj.delete()
      
    except Exception as e:
      print(e)
    return redirect('/see-blog/')
  return redirect('/login/')

def apropos(request):
  return render(request,'blog/post/apropos.html',)

def contact(request):
  return render(request,'blog/post/contact.html',)