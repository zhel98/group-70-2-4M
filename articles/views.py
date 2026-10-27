from django.shortcuts import render
from django.http.response import HttpResponse
from articles.models import Article

# Create your views here.


def hello_world(request):
    return HttpResponse('<h1>hello world<h1>')

def hello_e51an(request):
    return HttpResponse('я @e51an')

def article_list(request):
    articles = Article.objects.all()
    
    return HttpResponse(articles)