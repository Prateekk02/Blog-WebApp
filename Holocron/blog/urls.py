from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('<int:blog_id>/', views.blog_details, name="blog_details")
]