from django.contrib import admin
from articles.models import Article, Category, Todo

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Todo)

# Register your models here.
