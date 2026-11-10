"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from articles.views import (
    article_detail,
    article_list,
    todo_create,
    todo_detail,
    todo_list,
    todo_toggle,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todo_list, name='todo_list'),
    path('tasks/add/', todo_create, name='todo_create'),
    path('tasks/<int:pk>/', todo_detail, name='todo_detail'),
    path('tasks/<int:pk>/toggle/', todo_toggle, name='todo_toggle'),
    path('articles/', article_list, name='article_list'),
    path('articles/<int:id>/detail/', article_detail, name='article_detail'),
    path('<int:id>/detail/', article_detail, name='legacy_article_detail'),
]
