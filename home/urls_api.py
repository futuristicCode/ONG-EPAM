
from django.urls import path
from .views_api import *
from home import views_api

urlpatterns = [
    path('login/' , LoginView),
    # path('register/' , register_view)
    # path('register/', views_api.register_view ,name='register_view'),
]