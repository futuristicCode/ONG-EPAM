from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('',views.post_list,name='post_list'),
    path('membre/', views.membre_list ,name='membre_list'),
    path('partenaires/', views.partenaires_list ,name='partenaires_list'),
    path('login/', views.login_view ,name='login_view'),
    path('logout/', views.logout_view ,name='logout_view'),
    path('register/', views.register_view ,name='register_view'),
    path('add-blog/', views.add_blog ,name='add_blog'),
    path('see-blog/', views.see_blog ,name='see_blog'),
    path('update-blog/<pk>/', views.update_blog ,name='update_blog'),
    path('verify/<token>/', views.verify ,name='verify'),
    path('blog-delete/<id>/', views.blog_delete ,name='blog_delete'),
    path('apropos/', views.apropos ,name='apropos'),
    path('contact/', views.contact ,name='contact'),
   
    path('<slug>/',views.post_details,name='post_details'),
    
]
