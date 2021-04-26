"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin

from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
urlpatterns = [
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post-edit'),
    path('post/new/', BlogCreateView.as_view(), name='post-new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post-detail'),
    path('', BlogListView.as_view(), name='home'),


]
